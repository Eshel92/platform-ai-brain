<!-- Part 1 of 193 of reference/crd/k8ssandra-operator-crds-latest/_index.md (split because the page is big). -->

## config.k8ssandra.io/v1beta1

Resource Types:

- [ClientConfig](#clientconfig)




### ClientConfig
<sup><sup>[↩ Parent](#configk8ssandraiov1beta1 )</sup></sup>






ClientConfig is the Schema for the kubeconfigs API

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
      <td><b>apiVersion</b></td>
      <td>string</td>
      <td>config.k8ssandra.io/v1beta1</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b>kind</b></td>
      <td>string</td>
      <td>ClientConfig</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.20/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b><a href="#clientconfigspec">spec</a></b></td>
        <td>object</td>
        <td>
          ClientConfigSpec defines the desired state of KubeConfig<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


#### ClientConfig.spec
<sup><sup>[↩ Parent](#clientconfig)</sup></sup>



ClientConfigSpec defines the desired state of KubeConfig

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>contextName</b></td>
        <td>string</td>
        <td>
          ContextName allows to override the object name for context-name. If not set, the ClientConfig.Name is used as context name<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clientconfigspeckubeconfigsecret">kubeConfigSecret</a></b></td>
        <td>object</td>
        <td>
          KubeConfigSecret should reference an existing secret; the actual configuration will be read from
this secret's "kubeconfig" key.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


#### ClientConfig.spec.kubeConfigSecret
<sup><sup>[↩ Parent](#clientconfigspec)</sup></sup>



KubeConfigSecret should reference an existing secret; the actual configuration will be read from
this secret's "kubeconfig" key.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.
This field is effectively required, but due to backwards compatibility is
allowed to be empty. Instances of this type with an empty value here are
almost certainly wrong.
More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names<br/>
          <br/>
            <i>Default</i>: <br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>
