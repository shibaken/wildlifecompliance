<template lang="html">
    <div class="panel panel-default" >
      <div v-if="!hideHeader" class="panel-heading">
        <h3 class="panel-title">{{label}} 
            <a :href="'#'+section_id" class="panelClicker" data-toggle="collapse" expanded="true" :aria-controls="section_id">
                <span :class="panel_chevron_class"></span>
            </a>
        </h3>
      </div>
      <div :class="panel_collapse_class" :id="section_id">
          <slot></slot>
      </div>
    </div>
</template>

<script>
export default {
    name:"FormSection",
    props:[
        "label", 
        "Index", 
        "formCollapse", 
        "hideHeader",
        "treeHeight",
    ],
    data:function () {
        return {
            title:"Section title",
            eventInitialised: false,
            panel_chevron_class: null,
        }
    },
    computed:{
        section_id: function () {
            return "section_"+this.Index
        },
        panel_collapse_class: function() {
            if (this.formCollapse) {
                this.panel_chevron_class = "glyphicon glyphicon-chevron-down pull-right";
                return "panel-body collapse";
            } else {
                if (this.treeHeight) {
                    this.panel_chevron_class = "glyphicon glyphicon-chevron-up pull-right";
                    return "panel-body collapse in flex-container";
                } else {
                    this.panel_chevron_class = "glyphicon glyphicon-chevron-up pull-right";
                    return "panel-body collapse in";
                }
            }
        },

    },
    updated:function () {
        let vm = this;
        vm.$nextTick(()=>{
            if (!vm.eventInitialised){
                $('.panelClicker[data-toggle="collapse"]').on('click',function () {
                    var chev = $(this).children()[0];
            console.log(chev);
                    window.setTimeout(function () {
                        $(chev).toggleClass("glyphicon-chevron-down glyphicon-chevron-up");
                    },100);
                });
                this.eventInitialised = true;
            }
        });
    },
}
</script>

<style lang="css">
    h3.panel-title{
        font-weight: bold;
        font-size: 25px;
        padding:20px;
    }
    .flex-container {
        display: flex;
        flex-direction: column;
        min-height: 325px;
    }
    /*
    .tree-height{
        height: 5000px;
    }
    */
</style>
