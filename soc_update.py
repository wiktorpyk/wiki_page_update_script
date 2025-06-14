import re
import pyperclip
import time

template = """
{{Infobox soc
| manufacturer     = {manufacturer}
| name             = {name}
| image            = {image}
| model            = {model}
| codenames        = {codenames}
| arch             = {arch}
| year             = {year}
| process          = {process}
| cpu              = {cpu}
| gpu              = {gpu}
| npu              = {npu}
| isp              = {isp}
| modem            = {modem}
| mainline         = {mainline}
| community_page   = {community_page}
| related_issue    = {related_issue}
| related_post     = {related_post}

<!-- Features -->
<!-- 
For each of the following questions about device functionality, please respond as follows:
- Y for Yes     - if the feature works as expected
- P for Partial - if the feature works partially
- N for No      - if the feature does not work
- - for N/A     - if the feature is not applicable for the device
-   Leave blank - if the feature has not been tested
-->
| status_cpu       = {status_cpu} <!-- CPU support status -->
| status_uart      = {status_uart} <!-- UART support status -->
| status_storage   = {status_storage} <!-- Storage controller status -->
| status_usb       = {status_usb} <!-- USB controller status -->
| status_display   = {status_display} <!-- Display controller status -->
| status_gpu       = {status_gpu} <!-- GPU driver status -->
| status_pinctrl   = {status_pinctrl} <!-- Pin control subsystem status -->
| status_i2c       = {status_i2c} <!-- I2C bus status -->
| status_spi       = {status_spi} <!-- SPI bus status -->
| status_audio     = {status_audio} <!-- Audio subsystem status -->
| status_video     = {status_video} <!-- Video decoding/encoding status -->
| status_thermal   = {status_thermal} <!-- Thermal management status -->
| status_wifi      = {status_wifi} <!-- Wi-Fi status -->
| status_bluetooth = {status_bluetooth} <!-- Bluetooth status -->
| status_modem     = {status_modem} <!-- Cellular modem status -->
| status_gps       = {status_gps} <!-- GPS status -->
| status_camera    = {status_camera} <!-- Camera interface status -->
| status_suspend   = {status_suspend} <!-- Suspend/resume status -->
| status_npu       = {status_npu} <!-- Neural Processing Unit status -->
| status_ethernet  = {status_ethernet} <!-- Ethernet controller status -->
| status_sata      = {status_sata} <!-- SATA controller status -->
| status_pcie      = {status_pcie} <!-- PCI/PCIE controller status -->
}}
"""

template_empty = """
{{Infobox soc
| manufacturer     = <!-- e.g. Qualcomm -->
| name             = <!-- marketing name, e.g. Snapdragon 888 -->
| image            = <!-- File:CHANGE_ME_TO_SOC_MODEL.jpg -->
| model            = <!-- e.g. SM8350 -->
| codenames        = <!-- e.g. lahaina -->
| arch             = <!-- One of these: armhf, armv7, aarch64, riscv64, x86, x86_64 -->
| year             = <!-- Release year -->
| process          = <!-- Manufacturing process in nm -->
| cpu              = <!-- e.g. 4x 2.3 GHz Cortex-A53, 4x 1.8 GHz Cortex-A53 -->
| gpu              = <!-- e.g. Adreno 660 @ 840 MHz -->
| npu              = <!-- e.g. Hexagon 780 -->
| isp              = <!-- e.g. Spectra 580 -->
| modem            = <!-- e.g. 5G -->
| mainline         = <!-- Mainline Linux support (Yes/No) -->
| community_page   = <!-- URL to community page -->
| related_issue    = <!-- {{issue|CHANGE_ME|Pmaports}} -->
| related_post     = <!-- {{Lemmy|CHANGE_ME_TO_POST_ID}} -->


<!-- Features -->
<!-- 
For each of the following questions about device functionality, please respond as follows:
- Y for Yes     - if the feature works as expected
- P for Partial - if the feature works partially
- N for No      - if the feature does not work
- - for N/A     - if the feature is not applicable for the device
-   Leave blank - if the feature has not been tested
-->
| status_cpu       = - <!-- CPU support status -->
| status_uart      = - <!-- UART support status -->
| status_storage   = - <!-- Storage controller status -->
| status_usb       = - <!-- USB controller status -->
| status_display   = - <!-- Display controller status -->
| status_gpu       = - <!-- GPU driver status -->
| status_pinctrl   = - <!-- Pin control subsystem status -->
| status_i2c       = - <!-- I2C bus status -->
| status_spi       = - <!-- SPI bus status -->
| status_audio     = - <!-- Audio subsystem status -->
| status_video     = - <!-- Video decoding/encoding status -->
| status_thermal   = - <!-- Thermal management status -->
| status_wifi      = - <!-- Wi-Fi status -->
| status_bluetooth = - <!-- Bluetooth status -->
| status_modem     = - <!-- Cellular modem status -->
| status_gps       = - <!-- GPS status -->
| status_camera    = - <!-- Camera interface status -->
| status_suspend   = - <!-- Suspend/resume status -->
| status_npu       = - <!-- Neural Processing Unit status -->
| status_ethernet  = - <!-- Ethernet controller status -->
| status_sata      = - <!-- SATA controller status -->
| status_pcie      = - <!-- PCI/PCIE controller status -->
}}
"""

def parse_wiki_template(template_text):
    result = {}
    line_pattern = r'^\|\s*([^=]+?)\s*=\s*(.*)$'
    
    for i, line in enumerate(template_text.splitlines(), start=1):
        match = re.match(line_pattern, line)
        if match:
            key = match.group(1).strip()
            value = match.group(2).strip()
            
            # Remove trailing whitespace or newlines
            value = re.sub(r'\s+$', '', value, flags=re.MULTILINE)
            
            # Handle empty values
            if not value:
                value = ""
            
            # take out any newlines
            try:
                value = value.replace('\n', ' ').strip()
            except AttributeError: continue
            result[key] = value
        else:
            # Optional: debug print or log unrecognized lines
            pass  # or: print(f"Line {i} did not match: {line}")

    return result

def fill_template(base_template, empty_template, parsed_data):
    output = ""
    empty_template_lines = empty_template.splitlines()
    for i, line in enumerate(base_template.splitlines()):
        try:
            variable_search = re.search(r'\{(\w+)\}', line)
            if not variable_search: # If no placeholder, just add the line as is
                output += line + "\n"
                continue

            variable_name = variable_search.group(1)

            if variable_name in parsed_data:
                value = parsed_data[variable_name]
                if value == "": # If parsed value is an empty string
                    if variable_name.startswith("status_"):
                        # If the variable is a status variable and empty, fill with a space
                        output += line.replace(f"{{{variable_name}}}", " ") + "\n"
                    else:
                        # If not a status variable and empty, use the corresponding line from empty_template
                        output += empty_template_lines[i] + "\n"
                else:
                    # Parsed value is not empty, use it after cleaning
                    value_cleaned = re.sub(r'<!--.*?-->', '', value).strip()
                    output += line.replace(f"{{{variable_name}}}", value_cleaned) + "\n"
            else:
                # If the variable is not found in parsed_data, use the line from empty_template
                output += empty_template_lines[i] + "\n"
        except IndexError:
            # Fallback if empty_template_lines doesn't have a corresponding line (should not happen if templates match)
            output += line + "\n"
        except Exception: # General exception for regex or other issues
            output += line + "\n" # Add original line from base template if error
    return output.strip()


while True:
    wiki_template_input = pyperclip.paste()

    parsed_data = parse_wiki_template(wiki_template_input)
    # Use the SOC specific templates for filling
    filled_template = fill_template(template, template_empty, parsed_data)

    # Put the result into the clipboard
    pyperclip.copy(filled_template)
    input("Press Enter")