<!-- Part 1 of 8 of tutorial/prometheus-integration.md (split because the page is big). -->

## Prerequisites

- [Prometheus](https://prometheus.io/) integration is available in automation managed clusters that use MongoDB Agent 12.0.15.7646 or
  later. MongoDB Agent 12.0.15.7646 is released with Ops Manager 6.0.7.

- Have a working [Prometheus](https://prometheus.io/) instance. To set up a working instance, see
  their
  [Installation Guide](https://prometheus.io/docs/prometheus/latest/installation/).

- (Optional) Use [Grafana](https://prometheus.io/docs/visualization/grafana/) to
  visualize your Prometheus metrics.


## Procedure

To integrate Ops Manager with [Prometheus](https://prometheus.io/):

**Step 1: Navigate to the Integrations page for your project.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. Next to the Projects menu, expand the
   Options menu, then click Integrations.

**Step 2: Click Configure for the Prometheus integration card.**

**Step 3: Enter your preferred username and password.**

**Important:**

Copy your username and password in a secure location. You can't
access the password after you leave this screen.

**Step 4: Enter your IP address and port.**

**Tip:**

The default value, `0.0.0.0:9216`, scrapes metrics on port
`9216` on all IPv4 (Internet Protocol version 4) addresses on the local machine.

**Step 5: (Optional) Encrypt all Prometheus metrics.**

If you enable this setting, Ops Manager assures that your Prometheus
instance uses `https` to scrape metrics.

* - Fields
  - Description

* - TLS Certificate Key File Path
  -  `PEM` file path that contains certificate and key required
     to spin up a `https` Prometheus scraping endpoint. 

     You are responsible for the following:

     - TLS Certificate Key File issuance and renewal.
     - Checking if the endpoint started correctly in the automation agent logs.

* - TLS Certificate Key File Password
  - Required if the certificate key file is encrypted.

**Step 6: Select your preferred service discovery method.**

* - Discovery Method
  - Description

* - [HTTP SD](https://prometheus.io/docs/prometheus/latest/http_sd/)
  - This method requires Prometheus v2.28 and later. It
    generates the [scrape_config](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#scrape_config)
    part of your [configuration file](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#configuration-file)
    to discover targets over an HTTP endpoint.

* - [File Service Discovery](https://prometheus.io/docs/guides/file-sd/#use-file-based-service-discovery-to-discover-scrape-targets)
  - This method allows Prometheus to read YAML (Yet Another Markup Language) or JSON (Javascript Object Notation)
    documents to configure the targets to scrape from.

    You are responsible for providing the targets by making a request to the Discovery API and storing its results in a `targets.json` file.

    To make the request, substitute the placeholder text in one of
    the following tabs or create your own script in another language.

    **shell-command:**

    ```sh
    # Sets the `Authorization` header on every scrape
    # request with the username and password from the
    # previous step. The URL that Prometheus fetches the
    # targets from. 
    # Replace the <group-id> with the project ID of your
    # Ops Manager instance.

    curl --header 'Accept: application/json' \
         --user <username>:<password> \
         --request GET "https://cloud.mongodb.com/prometheus/v1.0/groups/{GROUP-ID}/discovery" 
    ```

    **python-script:**

    If you need to install the `requests` library,
    see their
    [Installation Guide](https://prometheus.io/docs/prometheus/latest/installation).

    ```python
    import time, json, requests

    # This script sets the `Authorization` header on every
    # scrape request with the configured username and
    # password. Then it tells Prometheus to fetch targets
    # from the specified URL. 
    #
    # Note: Replace the <username> and <password> with the
    # values in the previous step, and <group-id> with the
    # project ID of your Ops Manager instance.

    basic_auth_user="<username>"
    basic_auth_password="<password>"
    discovery_api_url="https://cloud.mongodb.com/prometheus/v1.0/groups/{GROUP-ID}/discovery"

    # The script updates your targets.json file every
    # minute, if it successfully retrieves targets.
    #
    # Note: Replace the <path-to-targets.json> with the
    # path to your targets.json file.

    starttime = time.time()
    while True:
      r = requests.get(discovery_api_url, auth=(basic_auth_user, basic_auth_password))
      if  r.status_code == 200:
        with open('<path-to-targets.json>', 'w') as f:
          json.dump(r.json(), f)
      time.sleep(60.0 - ((time.time() - starttime) % 60.0))
    ```

    To learn more about the Discovery API, see
    prometheus-discovery-endpoint-mms.

**Step 7: Click Save.**

**Step 8: View Your Cluster Metrics on Prometheus.**

a. Copy the generated snippet into the
   [scrape_configs](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#scrape_config) section of your 
   [configuration file](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#configuration-file)
   and substitute the placeholder text. 

   For an example of the configuration file in either method, see
   example-prometheus-configurations-mms.

#. Restart your Prometheus instance.

#. In your Prometheus instance, click `Status` in the top navigation
   bar, and click `Targets` to see the metrics of your deployment.


## Example Configurations

The following shows examples of the
[configuration file](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#configuration-file)
when you use the HTTP Service Discovery or
File Service Discovery method.

The configuration file in both methods contains the following fields:

| Field | Description |
|---|---|
| `scrape_interval` | Time that indicates how frequently to scrape targets. This setting supports a minimum time of 10s. |
| `job_name` | Human-readable label assigned to scraped metrics. |
| `metrics_path` | HTTP resource path that indicates where to fetch metrics from targets. |
| `scheme` | Your Prometheus protocol scheme configured for requests, either `http` or `https`. If you configure `https`, you must specify `tlsPemPath`. |
| `basic_auth` | Authorization header to use on every scrape request. |

  

### HTTP Service Discovery

The HTTP Service Discovery method also contains the `http_sd_configs`
field with the following sub-fields:

| Field | Description |
|---|---|
| `url` | URL from which Prometheus fetches the targets. |
| `refresh_interval` | Time that indicates when to re-query the endpoint. |
| `basic_auth` | Credentials to use for authenticating to the API server. |

```yaml
global:
  scrape_interval: 15s

scrape_configs:

  - job_name: "CM-Testing-mongo-metrics"
    scrape_interval: 10s
    metrics_path: /metrics
    scheme : https
    basic_auth:
      username: prom_user_61e6e34e93eac1632d39f457
      password: V7hTyLfkjwiWQbv
    http_sd_configs:
      - url: https://cloud.mongodb.com/prometheus/v1.0/groups/61e6e34e93eac1632d39f457/discovery
        refresh_interval: 60s
        basic_auth:
          username: prom_user_61e6e34e93eac1632d39f457
          password: V7hTyLfkjwiWQbv
```

### File Service Discovery

The File Service Discovery method also contains the
`file_sd_configs` field with the following sub-field:

| Field | Description |
|---|---|
| `files` | List that contains the files from which to extract the metrics scraping targets. |

```yaml
global:
  scrape_interval: 15s

scrape_configs:

  - job_name: "CM-Testing-mongo-metrics"
    scrape_interval: 10s
    metrics_path: /metrics
    scheme : https
    basic_auth:
      username: prom_user_61e6e34e93eac1632d39f457
      password: V7hTyLfkjwiWQbv
    file_sd_configs:
      - files:
        - /usr/local/etc/targets.json
```
