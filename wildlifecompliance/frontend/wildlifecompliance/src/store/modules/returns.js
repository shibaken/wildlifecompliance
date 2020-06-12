import Vue from 'vue';
import {
    UPDATE_RETURNS,
} from '@/store/mutation-types';

export const returnsStore = {
    state: {
        returns: {
            submitter: '',
            processing_status: '',
        },
    },
    getters: {
        return_id: state => state.returns.id,
        returns: state => state.returns,
        isReturnsLoaded: state => Object.keys(state.returns).length && state.returns.table != null,
    },
    mutations: {
        [UPDATE_RETURNS] (state, returns) {
            Vue.set(state, 'returns', {...returns});
        },
    },
    actions: {
        loadReturns({ dispatch, commit }, { url }) {
            return new Promise((resolve, reject) => {
                Vue.http.get(url).then(res => {

                    if (res.body.format !== 'sheet') {    // Return Sheets utilise Non-rendered data.
                        var obj = res.body.table[0]['data'][0]
                        for(let form_data_record of Object.keys(obj)) {
                            let deficiency_key = form_data_record + '-deficiency-field'    
                            dispatch('setFormValue', {
                                key: form_data_record,
                                value: {
                                    "value" :  obj[form_data_record], 
                                    "deficiency_value": obj[deficiency_key],                               
                                }
                            });

                        }
                    }

                    dispatch('setReturns', res.body);
                    resolve();
                },
                err => {
                    console.log(err);
                    reject();
                });
            })
        },
        setReturns({ dispatch, commit }, returns) {
            commit(UPDATE_RETURNS, returns);
        },
        refreshReturnFees({ dispatch, state, getters, rootGetters }) {
            Vue.http.post('/api/returns/' + getters.return_id + '/estimate_price/', {
                    'return_id': getters.return_id,
            }).then(res => {
                var obj = Object.values(res.body.fees)
                // dispatch('setReturns', {
                //     ...state.returns,
                //     return_fee: res.body.fees.return,
                // });
            }, err => {
                console.log(err);
            });
        },
    }
}
