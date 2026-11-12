<!-- Part 1 of 3 of reference/config-api/kubelet-config.v1beta1.md (split because the page is big). -->

## Resource Types 


- [CredentialProviderConfig](#kubelet-config-k8s-io-v1beta1-CredentialProviderConfig)
- [KubeletConfiguration](#kubelet-config-k8s-io-v1beta1-KubeletConfiguration)
- [SerializedNodeConfigSource](#kubelet-config-k8s-io-v1beta1-SerializedNodeConfigSource)
  
    
    


## `FormatOptions`     {#FormatOptions}
    

**Appears in:**

- [LoggingConfiguration](#LoggingConfiguration)


<p>FormatOptions contains options for the different logging formats.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>text</code> <B>[Required]</B><br/>
<a href="#TextOptions"><code>TextOptions</code></a>
</td>
<td>
   <p>[Alpha] Text contains options for logging format &quot;text&quot;.
Only available when the LoggingAlphaOptions feature gate is enabled.</p>
</td>
</tr>
<tr><td><code>json</code> <B>[Required]</B><br/>
<a href="#JSONOptions"><code>JSONOptions</code></a>
</td>
<td>
   <p>[Alpha] JSON contains options for logging format &quot;json&quot;.
Only available when the LoggingAlphaOptions feature gate is enabled.</p>
</td>
</tr>
</tbody>
</table>


## `JSONOptions`     {#JSONOptions}
    

**Appears in:**

- [FormatOptions](#FormatOptions)


<p>JSONOptions contains options for logging format &quot;json&quot;.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>OutputRoutingOptions</code> <B>[Required]</B><br/>
<a href="#OutputRoutingOptions"><code>OutputRoutingOptions</code></a>
</td>
<td>(Members of <code>OutputRoutingOptions</code> are embedded into this type.)
   <span class="text-muted">No description provided.</span></td>
</tr>
</tbody>
</table>


## `LogFormatFactory`     {#LogFormatFactory}
    


<p>LogFormatFactory provides support for a certain additional,
non-default log format.</p>





## `LoggingConfiguration`     {#LoggingConfiguration}
    

**Appears in:**

- [KubeletConfiguration](#kubelet-config-k8s-io-v1beta1-KubeletConfiguration)


<p>LoggingConfiguration contains logging options.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>format</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>Format Flag specifies the structure of log messages.
default value of format is <code>text</code></p>
</td>
</tr>
<tr><td><code>flushFrequency</code> <B>[Required]</B><br/>
<a href="#TimeOrMetaDuration"><code>TimeOrMetaDuration</code></a>
</td>
<td>
   <p>Maximum time between log flushes.
If a string, parsed as a duration (i.e. &quot;1s&quot;)
If an int, the maximum number of nanoseconds (i.e. 1s = 1000000000).
Ignored if the selected logging backend writes log messages without buffering.</p>
</td>
</tr>
<tr><td><code>verbosity</code> <B>[Required]</B><br/>
<a href="#VerbosityLevel"><code>VerbosityLevel</code></a>
</td>
<td>
   <p>Verbosity is the threshold that determines which log messages are
logged. Default is zero which logs only the most important
messages. Higher values enable additional messages. Error messages
are always logged.</p>
</td>
</tr>
<tr><td><code>vmodule</code> <B>[Required]</B><br/>
<a href="#VModuleConfiguration"><code>VModuleConfiguration</code></a>
</td>
<td>
   <p>VModule overrides the verbosity threshold for individual files.
Only supported for &quot;text&quot; log format.</p>
</td>
</tr>
<tr><td><code>options</code> <B>[Required]</B><br/>
<a href="#FormatOptions"><code>FormatOptions</code></a>
</td>
<td>
   <p>[Alpha] Options holds additional parameters that are specific
to the different logging formats. Only the options for the selected
format get used, but all of them get validated.
Only available when the LoggingAlphaOptions feature gate is enabled.</p>
</td>
</tr>
</tbody>
</table>


## `LoggingOptions`     {#LoggingOptions}
    


<p>LoggingOptions can be used with ValidateAndApplyWithOptions to override
certain global defaults.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>ErrorStream</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/io#Writer"><code>io.Writer</code></a>
</td>
<td>
   <p>ErrorStream can be used to override the os.Stderr default.</p>
</td>
</tr>
<tr><td><code>InfoStream</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/io#Writer"><code>io.Writer</code></a>
</td>
<td>
   <p>InfoStream can be used to override the os.Stdout default.</p>
</td>
</tr>
</tbody>
</table>


## `OutputRoutingOptions`     {#OutputRoutingOptions}
    

**Appears in:**

- [JSONOptions](#JSONOptions)

- [TextOptions](#TextOptions)


<p>OutputRoutingOptions contains options that are supported by both &quot;text&quot; and &quot;json&quot;.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>splitStream</code> <B>[Required]</B><br/>
<code>bool</code>
</td>
<td>
   <p>[Alpha] SplitStream redirects error messages to stderr while
info messages go to stdout, with buffering. The default is to write
both to stdout, without buffering. Only available when
the LoggingAlphaOptions feature gate is enabled.</p>
</td>
</tr>
<tr><td><code>infoBufferSize</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/api/resource#QuantityValue"><code>k8s.io/apimachinery/pkg/api/resource.QuantityValue</code></a>
</td>
<td>
   <p>[Alpha] InfoBufferSize sets the size of the info stream when
using split streams. The default is zero, which disables buffering.
Only available when the LoggingAlphaOptions feature gate is enabled.</p>
</td>
</tr>
</tbody>
</table>


## `TextOptions`     {#TextOptions}
    

**Appears in:**

- [FormatOptions](#FormatOptions)


<p>TextOptions contains options for logging format &quot;text&quot;.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>OutputRoutingOptions</code> <B>[Required]</B><br/>
<a href="#OutputRoutingOptions"><code>OutputRoutingOptions</code></a>
</td>
<td>(Members of <code>OutputRoutingOptions</code> are embedded into this type.)
   <span class="text-muted">No description provided.</span></td>
</tr>
</tbody>
</table>


## `TimeOrMetaDuration`     {#TimeOrMetaDuration}
    

**Appears in:**

- [LoggingConfiguration](#LoggingConfiguration)


<p>TimeOrMetaDuration is present only for backwards compatibility for the
flushFrequency field, and new fields should use metav1.Duration.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>Duration</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>Duration holds the duration</p>
</td>
</tr>
<tr><td><code>-</code> <B>[Required]</B><br/>
<code>bool</code>
</td>
<td>
   <p>SerializeAsString controls whether the value is serialized as a string or an integer</p>
</td>
</tr>
</tbody>
</table>


## `TracingConfiguration`     {#TracingConfiguration}
    

**Appears in:**

- [KubeletConfiguration](#kubelet-config-k8s-io-v1beta1-KubeletConfiguration)


<p>TracingConfiguration provides versioned configuration for OpenTelemetry tracing clients.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>endpoint</code><br/>
<code>string</code>
</td>
<td>
   <p>Endpoint of the collector this component will report traces to.
The connection is insecure, and does not currently support TLS.
Recommended is unset, and endpoint is the otlp grpc default, localhost:4317.</p>
</td>
</tr>
<tr><td><code>samplingRatePerMillion</code><br/>
<code>int32</code>
</td>
<td>
   <p>SamplingRatePerMillion is the number of samples to collect per million spans.
Recommended is unset. If unset, sampler respects its parent span's sampling
rate, but otherwise never samples.</p>
</td>
</tr>
</tbody>
</table>


## `VModuleConfiguration`     {#VModuleConfiguration}
    
(Alias of `[]k8s.io/component-base/logs/api/v1.VModuleItem`)

**Appears in:**

- [LoggingConfiguration](#LoggingConfiguration)


<p>VModuleConfiguration is a collection of individual file names or patterns
and the corresponding verbosity threshold.</p>





## `VerbosityLevel`     {#VerbosityLevel}
    
(Alias of `uint32`)

**Appears in:**

- [LoggingConfiguration](#LoggingConfiguration)



<p>VerbosityLevel represents a klog or logr verbosity threshold.</p>



  


## `CredentialProviderConfig`     {#kubelet-config-k8s-io-v1beta1-CredentialProviderConfig}
    


<p>CredentialProviderConfig is the configuration containing information about
each exec credential provider. Kubelet reads this configuration from disk and enables
each provider as specified by the CredentialProvider type.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>kubelet.config.k8s.io/v1beta1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>CredentialProviderConfig</code></td></tr>
    
  
<tr><td><code>providers</code> <B>[Required]</B><br/>
<a href="#kubelet-config-k8s-io-v1beta1-CredentialProvider"><code>[]CredentialProvider</code></a>
</td>
<td>
   <p>providers is a list of credential provider plugins that will be enabled by the kubelet.
Multiple providers may match against a single image, in which case credentials
from all providers will be returned to the kubelet. If multiple providers are called
for a single image, the results are combined. If providers return overlapping
auth keys, the value from the provider earlier in this list is attempted first.</p>
</td>
</tr>
</tbody>
</table>
