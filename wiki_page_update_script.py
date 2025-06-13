import re

template = """
{{Infobox device

<!-- Main -->
| manufacturer = {manufacturer}
| name         = {name}
| codename     = {codename}
| model        = {model}
| image        = {image}
| imagecaption = {imagecaption}
| releaseyear  = {releaseyear}
| prereleaseyear = {prereleaseyear}

| booting = {booting}
| status  = {status}

| packaged = {packaged}
| category = {category}


<!-- Hardware -->
| chipset = {chipset}
| cpu     = {cpu}
| gpu     = {gpu}
| som     = {som}
| display = {display}
| storage = {storage}
| memory  = {memory}
| architecture = {architecture}
| wp_type = {wp_type}


<!-- Software -->
| originalsoftware = {originalsoftware}
| originalversion  = {originalversion}
| extendedversion  = {extendedversion}
| optionalsoftware = {optionalsoftware}
| status_fossbootloader = {status_fossbootloader}


<!-- PostmarketOS -->
| type          = {type}
| pmoskernel    = {pmoskernel}
| whet_dhry     = {whet_dhry}
| genericdevice = {genericdevice}
| optionalgenericdevice = {optionalgenericdevice}
| kernelpackage = {kernelpackage}
| devicepackage = {devicepackage}
| firmwarepackage = {firmwarepackage}

<!-- Warning / Note boxes / Miscellaneous -->
| supported      = {supported}
| prebuiltimages = {prebuiltimages}
| boot_internal_storage = {boot_internal_storage}
| bootable_media = {bootable_media}
| changearch     = {changearch}

| initial_MR   = {initial_MR}
| related_post = {related_post}



<!-- Features -->
<!-- 
For each of the following questions about device functionality, please respond as follows:
- Y for Yes     - if the feature works as expected
- P for Partial - if the feature works partially
- N for No      - if the feature does not work
- - for N/A     - if the feature is not applicable for the device
-   Leave blank - if the feature has not been tested
-->

<!-- Main Features -->
| status_flashing = {status_flashing} <!-- Flashing with pmbootstrap -->
| status_usbnet   = {status_usbnet} <!-- USB networking -->
| status_emmc     = {status_emmc} <!-- Internal storage -->
| status_sdcard   = {status_sdcard} <!-- SD card support -->
| status_battery  = {status_battery} <!-- Battery percentage/charging -->
| status_screen   = {status_screen} <!-- Built-in display/embedded display connector -->
| status_touch    = {status_touch} <!-- Touchscreen -->
| status_keyboard = {status_keyboard} <!-- Build in Physical Keyboard -->
| status_touchpad = {status_touchpad} <!-- Build in Physical Touchpad -->
| status_stylus   = {status_stylus} <!-- Stylus/digital pen -->


<!-- Multimedia Features -->
| status_3d     = {status_3d} <!-- 3D acceleration -->
| status_dvb    = {status_dvb} <!-- TV tuner -->
| status_audio  = {status_audio} <!-- Speakers/headphones -->
| status_camera = {status_camera} <!-- Rear/front cameras -->
| status_cameraflash = {status_cameraflash} <!-- Flash/torch -->
| status_irtx   = {status_irtx} <!-- IR transmitter -->
| status_irrx   = {status_irrx} <!-- IR receiver -->


<!-- Connectivity Features -->
| status_wifi  = {status_wifi} <!-- Wi-Fi -->
| status_bluetooth = {status_bluetooth} <!-- Bluetooth -->
| status_ethernet = {status_ethernet} <!-- Wired Ethernet -->
| status_gps   = {status_gps} <!-- GPS -->
| status_nfc   = {status_nfc} <!-- NFC -->
| status_calls = {status_calls} <!-- Cellular calls -->
| status_sms   = {status_sms} <!-- SMS -->
| status_mobiledata = {status_mobiledata} <!-- Mobile data -->


<!-- Miscellaneous Features -->
| status_fde  = {status_fde} <!-- Full Disk Encryption -->
| status_usba = {status_usba} <!-- USB-A ports -->
| status_sata = {status_sata} <!-- SATA -->
| status_otg  = {status_otg} <!-- USB OTG -->
| status_hdmidp = {status_hdmidp} <!-- HDMI/DisplayPort -->


<!-- Sensors -->
| status_accel     = {status_accel} <!-- Accelerometer -->
| status_magnet    = {status_magnet} <!-- Magnetometer -->
| status_light     = {status_light} <!-- Ambient light -->
| status_proximity = {status_proximity} <!-- Proximity sensor -->
| status_hall      = {status_hall} <!-- Hall effect -->
| status_haptics   = {status_haptics} <!-- Vibration/haptics -->
| status_barometer = {status_barometer} <!-- Barometer -->
| status_powersensor = {status_powersensor} <!-- Power sensor -->


<!-- U-Boot (optional, for devices running U-Boot) -->
<!--
| status_uboot           = {status_uboot}
| status_uboot_primary   = {status_uboot_primary}
| status_uboot_secondary = {status_uboot_secondary}
| status_uboot_mainline  = {status_uboot_mainline}
| status_uboot_internalstorage = {status_uboot_internalstorage}
| status_uboot_sd        = {status_uboot_sd}
| status_uboot_usbhost   = {status_uboot_usbhost}
| status_uboot_usbperipheral = {status_uboot_usbperipheral}
| status_uboot_screen    = {status_uboot_screen}
| status_uboot_keyboard  = {status_uboot_keyboard}
| status_uboot_buttons   = {status_uboot_buttons}
-->
}}
"""

template_empty = """
{{Infobox device

<!-- Main -->
| manufacturer = <!-- e.g. Xiaomi -->
| name         = <!-- e.g. Redmi Note 13 Pro -->
| codename     = <!-- e.g. xiaomi-emerald -->
| model        = <!-- Manufacturer's model/part number, e.g. 2312DRA50G -->
| image        = File:CHANGE_ME_TO_DEVICE_CODENAME.jpg
| imagecaption = <!-- Brief description of the image -->
| releaseyear  = <!-- e.g. 2023 -->
| prereleaseyear = <!-- If the device was announced earlier than release -->

| booting = no <!-- *IMPORTANT* The device is booting at all, can be yes/no -->
| status  = <!-- Text displayed in the non-booting box, e.g "kernel compiles, doesn't boot" -->

| packaged = no <!-- yes if the device package has been merged into the pmaports repository -->
| category = <!-- main, community, testing, downstream -->


<!-- Hardware -->
| chipset = <!-- e.g. MediaTek Helio G99 (MT6789) -->
| cpu     = <!-- e.g. 2x 2.2 GHz Cortex-A76, 6x 2.0 GHz Cortex-A55 -->
| gpu     = <!-- e.g. Mali-G57 MC2 @ 850 MHz -->
| som     = <!-- Only applicable for carrier boards -->
| display = <!-- e.g. 1080 x 2400 AMOLED @ 120 Hz, 20:9, 6.67" -->
| storage = <!-- e.g. 128/256/512 GB -->
| memory  = <!-- e.g. 8/12 GB -->
| architecture = <!-- armhf, armv7, aarch64, riscv64, x86, x86_64 -->
| wp_type = 


<!-- Software -->
| originalsoftware = <!-- e.g. Android, Linux, Windows Phone -->
| originalversion  = <!-- e.g. 13 for Android 13 -->
| extendedversion  = <!-- Latest supported manufacturer OS version -->
| optionalsoftware = <!-- Other OS options -->
| status_fossbootloader = <!-- Y/P/N for FOSS bootloader -->


<!-- PostmarketOS -->
| type          = CHANGE_ME <!-- desktop, laptop, convertible, server, tablet, handset, watch, embedded, vm, see [[Device types]] -->
| pmoskernel    = <!-- Kernel version used in postmarketOS --> 
| whet_dhry     = <!-- UnixBench score, see [[Unixbench]] -->
| genericdevice = <!-- Name of the generic port page -->
| optionalgenericdevice = no <!-- yes to change the genericdevice box into an optional genericdevice box -->
| kernelpackage = <!-- {{Kernel package|device-codename|category}} -->
| devicepackage = <!-- {{Device package|device-codename|category}} -->
| firmwarepackage = <!-- {{Firmware package|device-codename|category}} -->

<!-- Warning / Note boxes / Miscellaneous -->
| supported      = yes <!-- no if device cannot run postmarketOS (see [[Category:Unsupported Devices]]) -->
| prebuiltimages = no  <!-- yes if prebuilt images are aviable on the pmOS website -->
| boot_internal_storage = <!-- no if the device can't boot from internal storage -->
| bootable_media = <!-- Specify the media type that can be used to boot pmOS, e.g "USB Stick" -->
| changearch     = <!-- Optional, text displayed in the "changearch" box, e.g "armv7" -->

| initial_MR   = <!-- {{MR|CHANGE_ME|pmaports}} -->
| related_post = <!-- {{Lemmy|CHANGE_ME_TO_POST_ID}} -->



<!-- Features -->
<!-- 
For each of the following questions about device functionality, please respond as follows:
- Y for Yes     - if the feature works as expected
- P for Partial - if the feature works partially
- N for No      - if the feature does not work
- - for N/A     - if the feature is not applicable for the device
-   Leave blank - if the feature has not been tested
-->

<!-- Main Features -->
| status_flashing = <!-- Flashing with pmbootstrap -->
| status_usbnet   = <!-- USB networking -->
| status_emmc     = <!-- Internal storage -->
| status_sdcard   = <!-- SD card support -->
| status_battery  = <!-- Battery percentage/charging -->
| status_screen   = <!-- Built-in display/embedded display connector -->
| status_touch    = <!-- Touchscreen -->
| status_keyboard = <!-- Build in Physical Keyboard -->
| status_touchpad = <!-- Build in Physical Touchpad -->
| status_stylus   = <!-- Stylus/digital pen -->


<!-- Multimedia Features -->
| status_3d     = <!-- 3D acceleration -->
| status_dvb    = <!-- TV tuner -->
| status_audio  = <!-- Speakers/headphones -->
| status_camera = <!-- Rear/front cameras -->
| status_cameraflash = <!-- Flash/torch -->
| status_irtx   = <!-- IR transmitter -->
| status_irrx   = <!-- IR receiver -->


<!-- Connectivity Features -->
| status_wifi  = <!-- Wi-Fi -->
| status_bluetooth = <!-- Bluetooth -->
| status_ethernet = <!-- Wired Ethernet -->
| status_gps   = <!-- GPS -->
| status_nfc   = <!-- NFC -->
| status_calls = <!-- Cellular calls -->
| status_sms   = <!-- SMS -->
| status_mobiledata = <!-- Mobile data -->


<!-- Miscellaneous Features -->
| status_fde  = <!-- Full Disk Encryption -->
| status_usba = <!-- USB-A ports -->
| status_sata = <!-- SATA -->
| status_otg  = <!-- USB OTG -->
| status_hdmidp = <!-- HDMI/DisplayPort -->


<!-- Sensors -->
| status_accel     = <!-- Accelerometer -->
| status_magnet    = <!-- Magnetometer -->
| status_light     = <!-- Ambient light -->
| status_proximity = <!-- Proximity sensor -->
| status_hall      = <!-- Hall effect -->
| status_haptics   = <!-- Vibration/haptics -->
| status_barometer = <!-- Barometer -->
| status_powersensor = <!-- Power sensor -->


<!-- U-Boot (optional, for devices running U-Boot) -->
<!--
| status_uboot           =
| status_uboot_primary   =
| status_uboot_secondary =
| status_uboot_mainline  =
| status_uboot_internalstorage =
| status_uboot_sd        =
| status_uboot_usbhost   =
| status_uboot_usbperipheral =
| status_uboot_screen    =
| status_uboot_keyboard  =
| status_uboot_buttons   =
-->

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
                value = None
                
            result[key] = value
        else:
            # Optional: debug print or log unrecognized lines
            pass  # or: print(f"Line {i} did not match: {line}")

    return result

def fill_template(template, template_empty, parsed_data):
    output = ""
    for i, line in enumerate(template.splitlines()):
        try:
            variable_name = re.search(r'\{(\w+)\}', line).group(0)[1:-1]
            if variable_name in parsed_data:
                value = parsed_data[variable_name]
                if value is None:
                    value = template_empty.splitlines()[i]
                    output += value + "\n"
                else:
                    output += line.replace(f"{{{variable_name}}}", value) + "\n"
            else:
                # If the variable is not found in parsed_data, use the empty template value
                value = template_empty.splitlines()[i]
                output += value + "\n"
        except:
            output += line + "\n"
    return output.strip()

wiki_template = """
{{Infobox device
| manufacturer = BQ
| name = Aquaris X5
| codename = bq-paella
| image = File:P_20200429_093001.jpg|thumb|133px
| imagecaption = BQ Aquaris X5 running Plasma Mobile on postmarketOS mainline
| releaseyear = 2015
| category = community
| originalsoftware = Android (CyanogenOS)
| originalversion = 5.1 (CyanogenOS 12.1)
| chipset = Qualcomm Snapdragon 412 (MSM8916v2)
| cpu = Quad-core 1.4 GHz Cortex-A53
| gpu = Adreno 306
| storage = 16GB / 32GB
| display = 720 x 1280 (IPS LCD capacitive touchscreen, 16M colors)
| memory = 2GB / 3GB
| architecture = aarch64
| type = handset
| status_usbnet = Y
| status_flashing = Y
| status_touch = Y
| status_screen = Y
| status_wifi = Y
| status_xwayland = Y
| status_fde = Y
| status_battery = Y
| status_3d = Y
| status_accel = Y
| status_audio = Y
| status_bluetooth = Y
| status_camera =
| status_gps = Y
| status_mobiledata = Y
| status_sms = Y
| status_calls = Y
| status_nfc = -
| status_irtx = -
| status =
| genericdevice=Generic MSM8916 (qcom-msm8916)
| optionalgenericdevice = yes
| booting = yes
| packaged = yes
| pmoskernel = Mainline
| whet_dhry = 913.7 <!-- NOTE: RESULT WITH FDE, PLEASE RE-TEST AND SUMBIT W/O IT; ALSO RE-TEST AFTER CPU WILL FINALLY RUN ON 1.4 GHZ -->
| status_otg = Y
}}
"""

parsed_data = parse_wiki_template(wiki_template)
filled_template = fill_template(template, template_empty, parsed_data)
print(filled_template)
