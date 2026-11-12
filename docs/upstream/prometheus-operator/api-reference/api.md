---
title: "API reference"
description: "Prometheus operator generated API reference docs"
draft: false
images: []
menu: "operator"
weight: 151
toc: true
---
> This page is automatically generated with `gen-crd-api-reference-docs`.
<p>Packages:</p>
<ul>
<li>
<a href="#monitoring.coreos.com%2fv1">monitoring.coreos.com/v1</a>
</li>
<li>
<a href="#monitoring.coreos.com%2fv1alpha1">monitoring.coreos.com/v1alpha1</a>
</li>
<li>
<a href="#monitoring.coreos.com%2fv1beta1">monitoring.coreos.com/v1beta1</a>
</li>
</ul>

<!-- This page was over 60 KB, so its sections are separate files. -->

## Sections (in `api.parts/`)

- `001-monitoring-coreos-com-v1.md`: monitoring.coreos.com/v1
- `002-monitoring-coreos-com-v1-alertmanager.md`: monitoring.coreos.com/v1 › Alertmanager
- `003-monitoring-coreos-com-v1-podmonitor.md`: monitoring.coreos.com/v1 › PodMonitor
- `004-monitoring-coreos-com-v1-probe.md`: monitoring.coreos.com/v1 › Probe
- `005-monitoring-coreos-com-v1-prometheus-part-1.md`: monitoring.coreos.com/v1 › Prometheus (part 1)
- `006-monitoring-coreos-com-v1-prometheus-part-2.md`: monitoring.coreos.com/v1 › Prometheus (part 2)
- `007-monitoring-coreos-com-v1-prometheusrule-servicemon.md`: monitoring.coreos.com/v1 › PrometheusRule … ServiceMonitor
- `008-monitoring-coreos-com-v1-thanosruler.md`: monitoring.coreos.com/v1 › ThanosRuler
- `009-monitoring-coreos-com-v1-apiserverconfig-alertmana.md`: monitoring.coreos.com/v1 › APIServerConfig … AlertmanagerGlobalConfig
- `010-monitoring-coreos-com-v1-alertmanagerlimitsspec.md`: monitoring.coreos.com/v1 › AlertmanagerLimitsSpec
- `011-monitoring-coreos-com-v1-alertmanagerspec.md`: monitoring.coreos.com/v1 › AlertmanagerSpec
- `012-monitoring-coreos-com-v1-alertmanagerstatus-client.md`: monitoring.coreos.com/v1 › AlertmanagerStatus … ClientAuthType
- `013-monitoring-coreos-com-v1-clustertlsconfig.md`: monitoring.coreos.com/v1 › ClusterTLSConfig
- `014-monitoring-coreos-com-v1-commonprometheusfields.md`: monitoring.coreos.com/v1 › CommonPrometheusFields
- `015-monitoring-coreos-com-v1-condition-dnspolicy.md`: monitoring.coreos.com/v1 › Condition … DNSPolicy
- `016-monitoring-coreos-com-v1-duration-enablefeature.md`: monitoring.coreos.com/v1 › Duration … EnableFeature
- `017-monitoring-coreos-com-v1-endpoint-globalsmtpconfig.md`: monitoring.coreos.com/v1 › Endpoint … GlobalSMTPConfig
- `018-monitoring-coreos-com-v1-globaltelegramconfig-http.md`: monitoring.coreos.com/v1 › GlobalTelegramConfig … HTTPConfigWithTLSFiles
- `019-monitoring-coreos-com-v1-httpconfigwithouttls-oaut.md`: monitoring.coreos.com/v1 › HTTPConfigWithoutTLS … OAuth2
- `020-monitoring-coreos-com-v1-otlpconfig-podmetricsendp.md`: monitoring.coreos.com/v1 › OTLPConfig … PodMetricsEndpoint
- `021-monitoring-coreos-com-v1-podmonitorspec-probespec.md`: monitoring.coreos.com/v1 › PodMonitorSpec … ProbeSpec
- `022-monitoring-coreos-com-v1-probetargetingress-promet.md`: monitoring.coreos.com/v1 › ProbeTargetIngress … PrometheusRuleSpec
- `023-monitoring-coreos-com-v1-prometheusspec-part-1.md`: monitoring.coreos.com/v1 › PrometheusSpec (part 1)
- `024-monitoring-coreos-com-v1-prometheusspec-part-2.md`: monitoring.coreos.com/v1 › PrometheusSpec (part 2)
- `025-monitoring-coreos-com-v1-prometheusstatus-reloadst.md`: monitoring.coreos.com/v1 › PrometheusStatus … ReloadStrategyType
- `026-monitoring-coreos-com-v1-remotereadspec-rule.md`: monitoring.coreos.com/v1 › RemoteReadSpec … Rule
- `027-monitoring-coreos-com-v1-rulegroup-servicediscover.md`: monitoring.coreos.com/v1 › RuleGroup … ServiceDiscoveryRole
- `028-monitoring-coreos-com-v1-servicemonitorspec-statef.md`: monitoring.coreos.com/v1 › ServiceMonitorSpec … StatefulSetUpdateStrategyType
- `029-monitoring-coreos-com-v1-storagespec-tsdbspec.md`: monitoring.coreos.com/v1 › StorageSpec … TSDBSpec
- `030-monitoring-coreos-com-v1-thanosrulerspec.md`: monitoring.coreos.com/v1 › ThanosRulerSpec
- `031-monitoring-coreos-com-v1-thanosrulerstatus-topolog.md`: monitoring.coreos.com/v1 › ThanosRulerStatus … TopologyShardingStrategy
- `032-monitoring-coreos-com-v1-topologyspreadconstraint-.md`: monitoring.coreos.com/v1 › TopologySpreadConstraint … WebHTTPHeaders
- `033-monitoring-coreos-com-v1-webtlsconfig-alertmanager.md`: monitoring.coreos.com/v1 › WebTLSConfig … AlertmanagerConfig
- `034-monitoring-coreos-com-v1alpha1-prometheusagent.md`: monitoring.coreos.com/v1alpha1 › PrometheusAgent
- `035-monitoring-coreos-com-v1alpha1-scrapeconfig.md`: monitoring.coreos.com/v1alpha1 › ScrapeConfig
- `036-monitoring-coreos-com-v1alpha1-alertmanagerconfigs.md`: monitoring.coreos.com/v1alpha1 › AlertmanagerConfigSpec … DayOfMonthRange
- `037-monitoring-coreos-com-v1alpha1-digitaloceansdconfi.md`: monitoring.coreos.com/v1alpha1 › DigitalOceanSDConfig … DockerSwarmSDConfig
- `038-monitoring-coreos-com-v1alpha1-ec2sdconfig-gcesdco.md`: monitoring.coreos.com/v1alpha1 › EC2SDConfig … GCESDConfig
- `039-monitoring-coreos-com-v1alpha1-httpconfig-ionossdc.md`: monitoring.coreos.com/v1alpha1 › HTTPConfig … IonosSDConfig
- `040-monitoring-coreos-com-v1alpha1-k8sselectorconfig-l.md`: monitoring.coreos.com/v1alpha1 › K8SSelectorConfig … LightSailSDConfig
- `041-monitoring-coreos-com-v1alpha1-linodesdconfig-noma.md`: monitoring.coreos.com/v1alpha1 › LinodeSDConfig … NomadSDConfig
- `042-monitoring-coreos-com-v1alpha1-ovhcloudsdconfig-op.md`: monitoring.coreos.com/v1alpha1 › OVHCloudSDConfig … OpsGenieConfigResponder
- `043-monitoring-coreos-com-v1alpha1-pagerdutyconfig-pro.md`: monitoring.coreos.com/v1alpha1 › PagerDutyConfig … PrometheusAgentMode
- `044-monitoring-coreos-com-v1alpha1-prometheusagentspec.md`: monitoring.coreos.com/v1alpha1 › PrometheusAgentSpec
- `045-monitoring-coreos-com-v1alpha1-puppetdbsdconfig-ro.md`: monitoring.coreos.com/v1alpha1 › PuppetDBSDConfig … RocketChatActionConfig
- `046-monitoring-coreos-com-v1alpha1-rocketchatconfig-sc.md`: monitoring.coreos.com/v1alpha1 › RocketChatConfig … ScalewaySDConfig
- `047-monitoring-coreos-com-v1alpha1-scrapeconfigspec.md`: monitoring.coreos.com/v1alpha1 › ScrapeConfigSpec
- `048-monitoring-coreos-com-v1alpha1-slackaction-timeran.md`: monitoring.coreos.com/v1alpha1 › SlackAction … TimeRange
- `049-monitoring-coreos-com-v1alpha1-url-dayofmonthrange.md`: monitoring.coreos.com/v1alpha1 › URL … DayOfMonthRange
- `050-monitoring-coreos-com-v1beta1-discordconfig-matcht.md`: monitoring.coreos.com/v1beta1 › DiscordConfig … MatchType
- `051-monitoring-coreos-com-v1beta1-matcher-parsedrange.md`: monitoring.coreos.com/v1beta1 › Matcher … ParsedRange
- `052-monitoring-coreos-com-v1beta1-pushoverconfig-rocke.md`: monitoring.coreos.com/v1beta1 › PushoverConfig … RocketChatFieldConfig
- `053-monitoring-coreos-com-v1beta1-route-slackconfirmat.md`: monitoring.coreos.com/v1beta1 › Route … SlackConfirmationField
- `054-monitoring-coreos-com-v1beta1-slackfield-webhookco.md`: monitoring.coreos.com/v1beta1 › SlackField … WebhookConfig
- `055-monitoring-coreos-com-v1beta1-weekday-yearrange.md`: monitoring.coreos.com/v1beta1 › Weekday … YearRange
