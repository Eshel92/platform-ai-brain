<!-- Part 13 of 55 of api-reference/api.md (split because the page is big). -->

<h3 id="monitoring.coreos.com/v1.ClusterTLSConfig">ClusterTLSConfig
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.AlertmanagerSpec">AlertmanagerSpec</a>)
</p>
<div>
<p>ClusterTLSConfig defines the mutual TLS configuration for the Alertmanager cluster TLS protocol.</p>
</div>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<code>server</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.WebTLSConfig">
WebTLSConfig
</a>
</em>
</td>
<td>
<p>server defines the server-side configuration for mutual TLS.</p>
</td>
</tr>
<tr>
<td>
<code>client</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.SafeTLSConfig">
SafeTLSConfig
</a>
</em>
</td>
<td>
<p>client defines the client-side configuration for mutual TLS.</p>
</td>
</tr>
</tbody>
</table>
