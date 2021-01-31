## API Root

```http request
GET krogoth_examples/


forum_viewsets/
AKThreadListView/
manual_post_method/
manual_post_reply/
simple_api/
contact/create/
contact/list/
contact/detail/<int:id>/
ram/
processes/
processesDummy/
storage/
cpuinfo/
uptime/




















```

```http request
GET admin_a9k/
```





```http request
GET global_static_interface/
\       load_static_css/<str:name>/
```
```http request
GET global_static_interface/
\       save_sqldb_to_filesystem/<str:name>/
```
```http request
GET global_static_interface/
\       save_filesystem_to_sqldb/<str:name>/
```
```http request
GET global_static_interface/
\      admin_editor_css/<str:name>/
```
```http request
POST global_static_interface/
\      admin_editor_css/<str:name>/
\      {
            "doc_name":"STYLE_MAIN", 
            "css_code":"/*lots of CSS code would go here. */", 
        }
```
```http request
PATCH global_static_interface/
\      admin_editor_css/<str:name>/
\      {
            "doc_name":"STYLE_MAIN", 
            "css_code":"/*lots of CSS code would go here. */", 
        }
```








```http request
GET moho_extractor/
\       KrogothFoundation?unique_name=coremodule
         LoadFileAsBase64?name=EpicPlanet_1.png
```
```http request
GET krogoth_gantry/
\        DynamicJavaScriptInjector ?name = Login
          DynamicHTMLInjector ?name = home
          DynamicHTMLSlaveInjector/
          MasterViewControllerEditorList/
          MasterViewControllerEditorDetail/
          SlaveViewControllerEditorList/
          SlaveViewControllerEditorDetail/
          KrogothAdministration/
              SaveSQLToFileSystem/
              CollectStatic/
              Compile/
          createNewMasterViewController/
          renameAngularJSService/
          createAngularJSService/
          renameAngularJSDirective/
          createAngularJSDirective/
          renameAngularJSTemplate/
          createAngularJSTemplate/
          renameJavaScriptTemplate/
```
```http request
GET krogoth_gantry/viewsets/
\          DynamicJavaScriptInjector/
            DynamicHTMLInjector/
            DynamicHTMLSlaveInjector/
            MasterViewControllerEditorList/
            MasterViewControllerEditorDetail/
            SlaveViewControllerEditorList/
            SlaveViewControllerEditorDetail/
```

```http request
GET rest-auth/
    user
```

```http request
GET api/
```

````http request
# Request:
GET krogoth_gantry/krogoth_examples/__ExamplesFruit
# Response:
    [{"name":"apple"}]
````

````http request
__ExamplesTextLabel
__ExamplesManufacturer
__ExamplesCar
__ExamplesTopping
__ExamplesPizza
__ExamplesHotel
__ExamplesOccupant
__ExamplesBasicImageUpload
__ExamplesBasicFileUpload
````