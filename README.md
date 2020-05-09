# Watermeter Reader Sensor
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs) ![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/hombrelab/home-assistant-watermeter-reader) ![GitHub commit activity](https://img.shields.io/github/last-commit/hombrelab/home-assistant-watermeter-reader)  
The [watermeter-reader](https://github.com/hombrelab/home-assistant-watermeter-reader) custom component for [home-assistant](https://www.home-assistant.io) is created to receive updates from the [hombre-watermeter-reader](https://github.com/hombrelab/hombre-watermeter-reader) Docker container.

The Hombre Watermeter Reader publishes a JSON object to an MQTT server.  

### Installation
Copy this folder to `<config_dir>/custom_components/watermeter_reader/` or use [hacs](https://github.com/custom-components/hacs) and point it to this [GitHub repository](https://github.com/hombrelab/home-assistant-watermeter-reader).  

Setup is done through the integration page:
- **topic**: _required_ MQTT topic the component has to subscribe to

Add the following to your `configuration.yaml` file:

After setting up the component you can create sensor templates to display the values nicely:
```yaml
---
# Watermeter Reader Cubic Meter
- platform: template
sensors:
  watermeter_cubic_meter:
    friendly_name: "Watermeter Cubic Meter"
    unit_of_measurement: m3
    value_template: >-
      {%- if states('sensor.watermeter_consumed') -%}
        {% set consumed = states('sensor.watermeter_consumed') | float / 1000 | round(3) %}
        {{consumed}}
      {%- else -%}
        -
      {%- endif -%}

# Watermeter Reader Updated
- platform: template
sensors:
  watermeter_updated:
    friendly_name: "Watermeter Updated"
    value_template: >-
      {%- if states('sensor.watermeter_timestamp') -%}
        {% set timestamp = states('sensor.watermeter_timestamp') | int | timestamp_custom('%H:%M:%S', true) %}
        {{timestamp}}
      {%- else -%}
        -
      {%- endif -%}
```
