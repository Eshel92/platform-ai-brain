<!-- Part 10 of 55 of api-reference/api.md (split because the page is big). -->

<h3 id="monitoring.coreos.com/v1.AlertmanagerLimitsSpec">AlertmanagerLimitsSpec
</h3>
<p>
(<em>Appears on:</em><a href="#monitoring.coreos.com/v1.AlertmanagerSpec">AlertmanagerSpec</a>)
</p>
<div>
<p>AlertmanagerLimitsSpec defines the limits command line flags when starting Alertmanager.</p>
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
<code>maxSilences</code><br/>
<em>
int32
</em>
</td>
<td>
<em>(Optional)</em>
<p>maxSilences defines the maximum number active and pending silences. This corresponds to the
Alertmanager&rsquo;s <code>--silences.max-silences</code> flag.
It requires Alertmanager &gt;= v0.28.0.</p>
</td>
</tr>
<tr>
<td>
<code>maxPerSilenceBytes</code><br/>
<em>
<a href="#monitoring.coreos.com/v1.ByteSize">
ByteSize
</a>
</em>
</td>
<td>
<em>(Optional)</em>
<p>maxPerSilenceBytes defines the maximum size of an individual silence as stored on disk. This corresponds to the Alertmanager&rsquo;s
<code>--silences.max-per-silence-bytes</code> flag.
It requires Alertmanager &gt;= v0.28.0.</p>
</td>
</tr>
</tbody>
</table>
