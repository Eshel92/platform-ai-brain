<!-- Part 3 of 3 of reference/kubernetes-api/policy-resources/validating-admission-policy-v1.md (split because the page is big). -->

## Operations {#Operations}



<hr>






### `get` read the specified ValidatingAdmissionPolicy

#### HTTP Request

GET /apis/admissionregistration.k8s.io/v1/validatingadmissionpolicies/{name}

#### Parameters


- **name** (*in path*): string, required

  name of the ValidatingAdmissionPolicy


- **pretty** (*in query*): string

  <a href="{{< ref "../common-parameters/common-parameters#pretty" >}}">pretty</a>



#### Response


200 (<a href="{{< ref "../policy-resources/validating-admission-policy-binding-v1#ValidatingAdmissionPolicy" >}}">ValidatingAdmissionPolicy</a>): OK

401: Unauthorized


### `get` read status of the specified ValidatingAdmissionPolicy

#### HTTP Request

GET /apis/admissionregistration.k8s.io/v1/validatingadmissionpolicies/{name}/status

#### Parameters


- **name** (*in path*): string, required

  name of the ValidatingAdmissionPolicy


- **pretty** (*in query*): string

  <a href="{{< ref "../common-parameters/common-parameters#pretty" >}}">pretty</a>



#### Response


200 (<a href="{{< ref "../policy-resources/validating-admission-policy-binding-v1#ValidatingAdmissionPolicy" >}}">ValidatingAdmissionPolicy</a>): OK

401: Unauthorized


### `list` list or watch objects of kind ValidatingAdmissionPolicy

#### HTTP Request

GET /apis/admissionregistration.k8s.io/v1/validatingadmissionpolicies

#### Parameters


- **allowWatchBookmarks** (*in query*): boolean

  <a href="{{< ref "../common-parameters/common-parameters#allowWatchBookmarks" >}}">allowWatchBookmarks</a>


- **continue** (*in query*): string

  <a href="{{< ref "../common-parameters/common-parameters#continue" >}}">continue</a>


- **fieldSelector** (*in query*): string

  <a href="{{< ref "../common-parameters/common-parameters#fieldSelector" >}}">fieldSelector</a>


- **labelSelector** (*in query*): string

  <a href="{{< ref "../common-parameters/common-parameters#labelSelector" >}}">labelSelector</a>


- **limit** (*in query*): integer

  <a href="{{< ref "../common-parameters/common-parameters#limit" >}}">limit</a>


- **pretty** (*in query*): string

  <a href="{{< ref "../common-parameters/common-parameters#pretty" >}}">pretty</a>


- **resourceVersion** (*in query*): string

  <a href="{{< ref "../common-parameters/common-parameters#resourceVersion" >}}">resourceVersion</a>


- **resourceVersionMatch** (*in query*): string

  <a href="{{< ref "../common-parameters/common-parameters#resourceVersionMatch" >}}">resourceVersionMatch</a>


- **sendInitialEvents** (*in query*): boolean

  <a href="{{< ref "../common-parameters/common-parameters#sendInitialEvents" >}}">sendInitialEvents</a>


- **timeoutSeconds** (*in query*): integer

  <a href="{{< ref "../common-parameters/common-parameters#timeoutSeconds" >}}">timeoutSeconds</a>


- **watch** (*in query*): boolean

  <a href="{{< ref "../common-parameters/common-parameters#watch" >}}">watch</a>



#### Response


200 (<a href="{{< ref "../policy-resources/validating-admission-policy-v1#ValidatingAdmissionPolicyList" >}}">ValidatingAdmissionPolicyList</a>): OK

401: Unauthorized


### `create` create a ValidatingAdmissionPolicy

#### HTTP Request

POST /apis/admissionregistration.k8s.io/v1/validatingadmissionpolicies

#### Parameters


- **body**: <a href="{{< ref "../policy-resources/validating-admission-policy-binding-v1#ValidatingAdmissionPolicy" >}}">ValidatingAdmissionPolicy</a>, required

  


- **dryRun** (*in query*): string

  <a href="{{< ref "../common-parameters/common-parameters#dryRun" >}}">dryRun</a>


- **fieldManager** (*in query*): string

  <a href="{{< ref "../common-parameters/common-parameters#fieldManager" >}}">fieldManager</a>


- **fieldValidation** (*in query*): string

  <a href="{{< ref "../common-parameters/common-parameters#fieldValidation" >}}">fieldValidation</a>


- **pretty** (*in query*): string

  <a href="{{< ref "../common-parameters/common-parameters#pretty" >}}">pretty</a>



#### Response


200 (<a href="{{< ref "../policy-resources/validating-admission-policy-binding-v1#ValidatingAdmissionPolicy" >}}">ValidatingAdmissionPolicy</a>): OK

201 (<a href="{{< ref "../policy-resources/validating-admission-policy-binding-v1#ValidatingAdmissionPolicy" >}}">ValidatingAdmissionPolicy</a>): Created

202 (<a href="{{< ref "../policy-resources/validating-admission-policy-binding-v1#ValidatingAdmissionPolicy" >}}">ValidatingAdmissionPolicy</a>): Accepted

401: Unauthorized


### `update` replace the specified ValidatingAdmissionPolicy

#### HTTP Request

PUT /apis/admissionregistration.k8s.io/v1/validatingadmissionpolicies/{name}

#### Parameters


- **name** (*in path*): string, required

  name of the ValidatingAdmissionPolicy


- **body**: <a href="{{< ref "../policy-resources/validating-admission-policy-binding-v1#ValidatingAdmissionPolicy" >}}">ValidatingAdmissionPolicy</a>, required

  


- **dryRun** (*in query*): string

  <a href="{{< ref "../common-parameters/common-parameters#dryRun" >}}">dryRun</a>


- **fieldManager** (*in query*): string

  <a href="{{< ref "../common-parameters/common-parameters#fieldManager" >}}">fieldManager</a>


- **fieldValidation** (*in query*): string

  <a href="{{< ref "../common-parameters/common-parameters#fieldValidation" >}}">fieldValidation</a>


- **pretty** (*in query*): string

  <a href="{{< ref "../common-parameters/common-parameters#pretty" >}}">pretty</a>



#### Response


200 (<a href="{{< ref "../policy-resources/validating-admission-policy-binding-v1#ValidatingAdmissionPolicy" >}}">ValidatingAdmissionPolicy</a>): OK

201 (<a href="{{< ref "../policy-resources/validating-admission-policy-binding-v1#ValidatingAdmissionPolicy" >}}">ValidatingAdmissionPolicy</a>): Created

401: Unauthorized


### `update` replace status of the specified ValidatingAdmissionPolicy

#### HTTP Request

PUT /apis/admissionregistration.k8s.io/v1/validatingadmissionpolicies/{name}/status

#### Parameters


- **name** (*in path*): string, required

  name of the ValidatingAdmissionPolicy


- **body**: <a href="{{< ref "../policy-resources/validating-admission-policy-binding-v1#ValidatingAdmissionPolicy" >}}">ValidatingAdmissionPolicy</a>, required

  


- **dryRun** (*in query*): string

  <a href="{{< ref "../common-parameters/common-parameters#dryRun" >}}">dryRun</a>


- **fieldManager** (*in query*): string

  <a href="{{< ref "../common-parameters/common-parameters#fieldManager" >}}">fieldManager</a>


- **fieldValidation** (*in query*): string

  <a href="{{< ref "../common-parameters/common-parameters#fieldValidation" >}}">fieldValidation</a>


- **pretty** (*in query*): string

  <a href="{{< ref "../common-parameters/common-parameters#pretty" >}}">pretty</a>



#### Response


200 (<a href="{{< ref "../policy-resources/validating-admission-policy-binding-v1#ValidatingAdmissionPolicy" >}}">ValidatingAdmissionPolicy</a>): OK

201 (<a href="{{< ref "../policy-resources/validating-admission-policy-binding-v1#ValidatingAdmissionPolicy" >}}">ValidatingAdmissionPolicy</a>): Created

401: Unauthorized


### `patch` partially update the specified ValidatingAdmissionPolicy

#### HTTP Request

PATCH /apis/admissionregistration.k8s.io/v1/validatingadmissionpolicies/{name}

#### Parameters


- **name** (*in path*): string, required

  name of the ValidatingAdmissionPolicy


- **body**: <a href="{{< ref "../common-definitions/patch#Patch" >}}">Patch</a>, required

  


- **dryRun** (*in query*): string

  <a href="{{< ref "../common-parameters/common-parameters#dryRun" >}}">dryRun</a>


- **fieldManager** (*in query*): string

  <a href="{{< ref "../common-parameters/common-parameters#fieldManager" >}}">fieldManager</a>


- **fieldValidation** (*in query*): string

  <a href="{{< ref "../common-parameters/common-parameters#fieldValidation" >}}">fieldValidation</a>


- **force** (*in query*): boolean

  <a href="{{< ref "../common-parameters/common-parameters#force" >}}">force</a>


- **pretty** (*in query*): string

  <a href="{{< ref "../common-parameters/common-parameters#pretty" >}}">pretty</a>



#### Response


200 (<a href="{{< ref "../policy-resources/validating-admission-policy-binding-v1#ValidatingAdmissionPolicy" >}}">ValidatingAdmissionPolicy</a>): OK

201 (<a href="{{< ref "../policy-resources/validating-admission-policy-binding-v1#ValidatingAdmissionPolicy" >}}">ValidatingAdmissionPolicy</a>): Created

401: Unauthorized


### `patch` partially update status of the specified ValidatingAdmissionPolicy

#### HTTP Request

PATCH /apis/admissionregistration.k8s.io/v1/validatingadmissionpolicies/{name}/status

#### Parameters


- **name** (*in path*): string, required

  name of the ValidatingAdmissionPolicy


- **body**: <a href="{{< ref "../common-definitions/patch#Patch" >}}">Patch</a>, required

  


- **dryRun** (*in query*): string

  <a href="{{< ref "../common-parameters/common-parameters#dryRun" >}}">dryRun</a>


- **fieldManager** (*in query*): string

  <a href="{{< ref "../common-parameters/common-parameters#fieldManager" >}}">fieldManager</a>


- **fieldValidation** (*in query*): string

  <a href="{{< ref "../common-parameters/common-parameters#fieldValidation" >}}">fieldValidation</a>


- **force** (*in query*): boolean

  <a href="{{< ref "../common-parameters/common-parameters#force" >}}">force</a>


- **pretty** (*in query*): string

  <a href="{{< ref "../common-parameters/common-parameters#pretty" >}}">pretty</a>



#### Response


200 (<a href="{{< ref "../policy-resources/validating-admission-policy-binding-v1#ValidatingAdmissionPolicy" >}}">ValidatingAdmissionPolicy</a>): OK

201 (<a href="{{< ref "../policy-resources/validating-admission-policy-binding-v1#ValidatingAdmissionPolicy" >}}">ValidatingAdmissionPolicy</a>): Created

401: Unauthorized


### `delete` delete a ValidatingAdmissionPolicy

#### HTTP Request

DELETE /apis/admissionregistration.k8s.io/v1/validatingadmissionpolicies/{name}

#### Parameters


- **name** (*in path*): string, required

  name of the ValidatingAdmissionPolicy


- **body**: <a href="{{< ref "../common-definitions/delete-options#DeleteOptions" >}}">DeleteOptions</a>

  


- **dryRun** (*in query*): string

  <a href="{{< ref "../common-parameters/common-parameters#dryRun" >}}">dryRun</a>


- **gracePeriodSeconds** (*in query*): integer

  <a href="{{< ref "../common-parameters/common-parameters#gracePeriodSeconds" >}}">gracePeriodSeconds</a>


- **ignoreStoreReadErrorWithClusterBreakingPotential** (*in query*): boolean

  <a href="{{< ref "../common-parameters/common-parameters#ignoreStoreReadErrorWithClusterBreakingPotential" >}}">ignoreStoreReadErrorWithClusterBreakingPotential</a>


- **pretty** (*in query*): string

  <a href="{{< ref "../common-parameters/common-parameters#pretty" >}}">pretty</a>


- **propagationPolicy** (*in query*): string

  <a href="{{< ref "../common-parameters/common-parameters#propagationPolicy" >}}">propagationPolicy</a>



#### Response


200 (<a href="{{< ref "../common-definitions/status#Status" >}}">Status</a>): OK

202 (<a href="{{< ref "../common-definitions/status#Status" >}}">Status</a>): Accepted

401: Unauthorized


### `deletecollection` delete collection of ValidatingAdmissionPolicy

#### HTTP Request

DELETE /apis/admissionregistration.k8s.io/v1/validatingadmissionpolicies

#### Parameters


- **body**: <a href="{{< ref "../common-definitions/delete-options#DeleteOptions" >}}">DeleteOptions</a>

  


- **continue** (*in query*): string

  <a href="{{< ref "../common-parameters/common-parameters#continue" >}}">continue</a>


- **dryRun** (*in query*): string

  <a href="{{< ref "../common-parameters/common-parameters#dryRun" >}}">dryRun</a>


- **fieldSelector** (*in query*): string

  <a href="{{< ref "../common-parameters/common-parameters#fieldSelector" >}}">fieldSelector</a>


- **gracePeriodSeconds** (*in query*): integer

  <a href="{{< ref "../common-parameters/common-parameters#gracePeriodSeconds" >}}">gracePeriodSeconds</a>


- **ignoreStoreReadErrorWithClusterBreakingPotential** (*in query*): boolean

  <a href="{{< ref "../common-parameters/common-parameters#ignoreStoreReadErrorWithClusterBreakingPotential" >}}">ignoreStoreReadErrorWithClusterBreakingPotential</a>


- **labelSelector** (*in query*): string

  <a href="{{< ref "../common-parameters/common-parameters#labelSelector" >}}">labelSelector</a>


- **limit** (*in query*): integer

  <a href="{{< ref "../common-parameters/common-parameters#limit" >}}">limit</a>


- **pretty** (*in query*): string

  <a href="{{< ref "../common-parameters/common-parameters#pretty" >}}">pretty</a>


- **propagationPolicy** (*in query*): string

  <a href="{{< ref "../common-parameters/common-parameters#propagationPolicy" >}}">propagationPolicy</a>


- **resourceVersion** (*in query*): string

  <a href="{{< ref "../common-parameters/common-parameters#resourceVersion" >}}">resourceVersion</a>


- **resourceVersionMatch** (*in query*): string

  <a href="{{< ref "../common-parameters/common-parameters#resourceVersionMatch" >}}">resourceVersionMatch</a>


- **sendInitialEvents** (*in query*): boolean

  <a href="{{< ref "../common-parameters/common-parameters#sendInitialEvents" >}}">sendInitialEvents</a>


- **timeoutSeconds** (*in query*): integer

  <a href="{{< ref "../common-parameters/common-parameters#timeoutSeconds" >}}">timeoutSeconds</a>



#### Response


200 (<a href="{{< ref "../common-definitions/status#Status" >}}">Status</a>): OK

401: Unauthorized
