<!-- Converted from setup/starting.asciidoc (AsciiDoc). Includes are inlined. -->

## Starting Elasticsearch

The method for starting Elasticsearch varies depending on how you installed it. 

### Archive packages (`.tar.gz`)

If you installed Elasticsearch with a `.tar.gz` package, you can start Elasticsearch from the 
command line.  

(See `setup/install/targz-start.md`)
(See `setup/install/targz-daemon.md`)

### Archive packages (`.zip`)

If you installed Elasticsearch on Windows with a `.zip` package, you can start Elasticsearch from 
the command line. If you want Elasticsearch to start automatically at boot time without 
any user interaction, install Elasticsearch as a service.

(See `setup/install/zip-windows-start.md`)

### Debian packages

(See `setup/install/systemd.md`)

### Docker images

If you installed a Docker image, you can start Elasticsearch from the command line. There 
are different methods depending on whether you're using development mode or 
production mode. See docker-cli-run-dev-mode. 

### RPM packages

(See `setup/install/systemd.md`)
