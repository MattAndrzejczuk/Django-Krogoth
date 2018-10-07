(function() {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .directive('_DJANGULAR_DIRECTIVE_NAME_', _DJANGULAR_DIRECTIVE_NAME_Directive);
    /** @ngInject */
    function _DJANGULAR_DIRECTIVE_NAME_Directive($compile, $log) {









        return {
            restrict: 'A',
            link: function(scope, element, attrs) {





                $log.log("FUCKING TREE VIEW LOADED....");
                $log.log("");





                //tree id
                var treeId = attrs.treeId;
                //tree model
                var treeModel = attrs.treeModel;
                //node id
                var nodeId = attrs.nodeId || 'id';
                //node label
                var nodeLabel = attrs.nodeLabel || 'label';
                //children
                var nodeChildren = attrs.nodeChildren || 'children';
                //tree template
                var template =
                    '<ul>' +
                    '<li data-ng-repeat="node in ' + treeModel + '">' +
                    '<i class="collapsed" data-ng-show="node.' + nodeChildren +
                    '.length && node.collapsed" data-ng-click="' + treeId +
                    '.selectNodeHead(node)"></i>' +
                    '<i class="expanded" data-ng-show="node.' + nodeChildren +
                    '.length && !node.collapsed" data-ng-click="' + treeId +
                    '.selectNodeHead(node)"></i>' +
                    '<i class="normal" data-ng-hide="node.' + nodeChildren +
                    '.length"></i> ' +
                    '<span data-ng-class="node.selected" data-ng-click="' +
                    treeId + '.selectNodeLabel(node)">{{node.' + nodeLabel +
                    '}}</span>' +
                    '<div data-ng-hide="node.collapsed" data-tree-id="' + treeId +
                    '" data-tree-model="node.' + nodeChildren + '" data-node-id=' +
                    nodeId + ' data-node-label=' + nodeLabel + ' data-node-children=' +
                    nodeChildren + '></div>' +
                    '</li>' +
                    '</ul>';
                //check tree id, tree model
                if (treeId && treeModel) {
                    //root node
                    $log.log("treeId && treeModel");
                    if (attrs.angularTreeview) {
                        $log.log("attrs.angularTreeview");
                        //create tree object if not exists
                        scope[treeId] = scope[treeId] || {};
                        //if node head clicks,
                        scope[treeId].selectNodeHead = scope[treeId].selectNodeHead || function(selectedNode) {

                            //Collapse or Expand
                            selectedNode.collapsed = !selectedNode.collapsed;
                        };
                        //if node label clicks,
                        scope[treeId].selectNodeLabel = scope[treeId].selectNodeLabel || function(selectedNode) {
                            //remove highlight from previous node
                            if (scope[treeId].currentNode && scope[treeId].currentNode.selected) {
                                scope[treeId].currentNode.selected = undefined;
                            }
                            //set highlight to selected node
                            selectedNode.selected = 'selected';
                            //set currentNode
                            scope[treeId].currentNode = selectedNode;
                        };
                    } else {

                        $log.log("TREE VIEW FUCKED UP: attrs.angularTreeview");

                    }
                    //Rendering template.
                    element.html('').append($compile(template)(scope));
                } else {

                    $log.log("TREE VIEW FUCKED UP: treeId && treeModel");

                }









            }









        };









    }
})
();