/*
GET   http://localhost:8000/global_static_text/load_static_text_readonly/AKCustom.frostedGlassdirective.es6
 */
(function () {
    'use strict';
    angular
        .module('app.core')
        .directive('akFrostedGlass', akFrostedGlassDirective);

    /** @ngInject */
    function akFrostedGlassDirective($interval) {

		console.log(' ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ akFrostedGlass ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ');
        console.log(' ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ akFrostedGlass ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ');
        console.log(' ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ akFrostedGlass ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ');
        console.log(' ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ akFrostedGlass ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ');
        console.log(' ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ akFrostedGlass ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ');


        return {
            // scope: {
            //     offset: "@offset",
            //     scrollClass: '='
            // },
            link: function (scope, element, attr) {
                function updateTime() {
                    //const childPos = element.offset();
                    //const childHeight = element.height();
                    //const parentoffset = element.parent().offset();
                    //const parentHeight = element.parent().height();

                    const y = (element.offset().top * -1) + 'px';
                    const x = (element.offset().left * -1) + 'px';

                    element.css({
                        backgroundPositionY: y,
                        backgroundPositionX: x
                    });

                }

                var stopTime = $interval(updateTime, 100);

                element.on('$destroy', function () {
                    console.log('akFrostedGlass $destroyed');
                    $interval.cancel(stopTime);
                });
            }
        }
    }
})
();



/* ~ ~ ~ ~ ~ ~ ~ ~ ANGULARJS 1.7.2 ~ ~ ~ ~ ~ ~ ~ ~ */
(function () {
    'use strict';
    angular
        .module('app.core')
        .directive('kgTreeView', kgTreeViewDirective);

    /** @ngInject */
    function kgTreeViewDirective() {
        return {
            restrict: 'A',
            link: function (scope, element, attrs) {
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
                    if (attrs.angularTreeview) {
                        //create tree object if not exists
                        scope[treeId] = scope[treeId] || {};
                        //if node head clicks,
                        scope[treeId].selectNodeHead = scope[treeId].selectNodeHead || function (selectedNode) {

                            //Collapse or Expand
                            selectedNode.collapsed = !selectedNode.collapsed;
                        };
                        //if node label clicks,
                        scope[treeId].selectNodeLabel = scope[treeId].selectNodeLabel || function (selectedNode) {
                            //remove highlight from previous node
                            if (scope[treeId].currentNode && scope[treeId].currentNode.selected) {
                                scope[treeId].currentNode.selected = undefined;
                            }
                            //set highlight to selected node
                            selectedNode.selected = 'selected';
                            //set currentNode
                            scope[treeId].currentNode = selectedNode;
                        };
                    }
                    //Rendering template.
                    element.html('').append($compile(template)(scope));
                }
            }
        };
    }
})();