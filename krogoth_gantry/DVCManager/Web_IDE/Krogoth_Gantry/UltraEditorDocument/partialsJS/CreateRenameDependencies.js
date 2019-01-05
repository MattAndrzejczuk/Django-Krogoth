vm.createNewComponentClick = createNewComponentClick;
vm.addNewComponentToMaster = addNewComponentToMaster;
vm.renameObjectForm = {};
vm.renameObjectSubmit = renameObjectSubmit;



function createNewComponentClick(ev, treeRoot) {
            var siblings = treeRoot.nodes;

            var djangoModelName = (treeRoot.class);
            ///var djangoModelName = SaveToSQL.getRESTfulModelName(treeRoot.class);

            $log.debug('---createNewComponentClick---');
            $log.log("treeRoot: ");
            $log.log(treeRoot);
            $log.debug('TODO FINISH THIS PART ! ! !');

            var confirm = $mdDialog.prompt()
                .title('Create new ' + djangoModelName)
                .textContent('Unique ' + djangoModelName + ' file name:')
                .placeholder(djangoModelName + '.js')
                .ariaLabel('Unique ' + djangoModelName + ' file name:')
                .initialValue('')
                .targetEvent(ev)
                .ok('Ok')
                .cancel('Cancel');
            $mdDialog.show(confirm).then(function(new_name) {

                const postPayload = {
                    "path_0": vm.finishedBreadCrumbsJson._1st.name,
                    "path_1": vm.finishedBreadCrumbsJson._2nd.name,
                    "master_name": vm.masterName,
                    "index": treeRoot.nodes.length,
                    "new_name": new_name
                };

                if (djangoModelName === "Directive") {
                    DirectiveCRUD.createDirective(postPayload)
                        .then(function(newTreeNode) {
                            $log.log("CREATE FINISHED");
                            $log.debug(newTreeNode);
                            const parentI = newTreeNode.parentIndex;
                            vm.treeData[parentI].nodes.push(newTreeNode);
                        });

                } else if (djangoModelName === "Service") {
                    fileNameChanger.createService(postPayload)
                        .then(function(newTreeNode) {
                            $log.log("CREATE FINISHED");
                            $log.debug(newTreeNode);
                            const parentI = newTreeNode.parentIndex;
                            vm.treeData[parentI].nodes.push(newTreeNode);
                        });

                } else if (treeRoot.class === "Template") {

                    TemplateCRUD.createTemplate(postPayload)
                        .then(function(newTreeNode) {
                            $log.log("CREATE FINISHED");
                            $log.debug(newTreeNode);
                            const parentI = newTreeNode.parentIndex;
                            vm.treeData[parentI].nodes.push(newTreeNode);
                        });
                } else if (treeRoot.class === "TemplateJS") {

                    TemplateCRUD.createJSTemplate(postPayload)
                        .then(function(newTreeNode) {
                            $log.log("CREATE FINISHED");
                            $log.debug(newTreeNode);
                            const parentI = newTreeNode.parentIndex;
                            vm.treeData[parentI].nodes.push(newTreeNode);
                        });
                } else {
                    $log.info("UNKNOWN TREE CLASS: " + treeRoot.class);
                }
            }, function() {});
        }


        function renameObjectSubmit() {
            const _0 = vm.finishedBreadCrumbsJson._1st.name;
            const _1 = vm.finishedBreadCrumbsJson._2nd.name;
            const _2 = vm.masterName;
            const objectToRename = vm.treeData[vm.loadedParentIndex].nodes[vm.loadedIndex].class;
            $log.debug("RENAME OBJECT DID FINISH SUBMIT");
            $log.debug(objectToRename);
            if (objectToRename === "Service") {
                fileNameChanger.renameService(_0,
                        _1,
                        _2,
                        vm.treeData[vm.loadedParentIndex].nodes[vm.loadedIndex].name,
                        vm.renameObjectForm.new)
                    .then(function(didFinish) {
                        $log.debug("The rename service operation finished on the server.");
                        $log.debug(didFinish);
                        vm.treeData[vm.loadedParentIndex].nodes[vm.loadedIndex].name = vm.renameObjectForm.new;
                        vm.treeData[vm.loadedParentIndex].nodes[vm.loadedIndex].title = vm.renameObjectForm.new;
                        vm.renameObjectForm.new = "";
                        /// success
                    });
            } else if (objectToRename === "Directive") {
                DirectiveCRUD.renameDirective(_0,
                        _1,
                        _2,
                        vm.treeData[vm.loadedParentIndex].nodes[vm.loadedIndex].name,
                        vm.renameObjectForm.new)
                    .then(function(didFinish) {
                        $log.debug("The rename service operation finished on the server.");
                        $log.debug(didFinish);
                        vm.treeData[vm.loadedParentIndex].nodes[vm.loadedIndex].name = vm.renameObjectForm.new;
                        vm.treeData[vm.loadedParentIndex].nodes[vm.loadedIndex].title = vm.renameObjectForm.new;
                        vm.renameObjectForm.new = "";
                        /// success
                    });
            } else if (objectToRename === "NgIncludedHtml") {
                TemplateCRUD.renameJSTemplate(_0,
                        _1,
                        _2,
                        vm.treeData[vm.loadedParentIndex].nodes[vm.loadedIndex].name,
                        vm.renameObjectForm.new)
                    .then(function(didFinish) {
                        $log.debug("The rename service operation finished on the server.");
                        $log.debug(didFinish);
                        vm.treeData[vm.loadedParentIndex].nodes[vm.loadedIndex].name = vm.renameObjectForm.new;
                        vm.treeData[vm.loadedParentIndex].nodes[vm.loadedIndex].title = vm.renameObjectForm.new;
                        vm.renameObjectForm.new = "";
                        /// success
                    });
            } else if (objectToRename === "NgIncludedJs") {
                TemplateCRUD.renameJSTemplate(_0,
                        _1,
                        _2,
                        vm.treeData[vm.loadedParentIndex].nodes[vm.loadedIndex].name,
                        vm.renameObjectForm.new)
                    .then(function(didFinish) {
                        //var i = vm.loadedParentIndex;
                        //var j = vm.loadedIndex;
                        $log.debug("The rename service operation finished on the server.");
                        $log.debug(didFinish);
                        vm.treeData[vm.loadedParentIndex].nodes[vm.loadedIndex].name = vm.renameObjectForm.new;
                        vm.treeData[vm.loadedParentIndex].nodes[vm.loadedIndex].title = vm.renameObjectForm.new;

                        //const srdId = i.toString() + "-" + j.toString();
                        //const srcTitle = "_" + vm.treeData[i].nodes[j].title;
                        //const key = srdId + srcTitle;
                        //vm.srcMap[key] = vm.srcHolder.length.toString();

                        vm.renameObjectForm.new = "";
                        /// success
                    });
            }
        }


        function addNewComponentToMaster(siblings, newNode, djangoModelName, masterId) {
            SaveToSQL.addSiblingToMaster(siblings, newNode, djangoModelName, masterId)
                .then(function(newNodeForTree) {
                    $log.debug('newNodeForTree:');
                    $log.log(newNodeForTree);
                    $log.debug('TODO FINISH THIS PART ! ! !');
                });
        }