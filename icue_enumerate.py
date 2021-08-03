import os
from cuesdk import CueSdk

sdk = CueSdk(os.path.join(os.getcwd(), 'bin\\CUESDK.x64_2017.dll'))
sdk.connect()
print('')
print(122 * '-')
print(50 * '-', '[ICUE ENUMERATOR]', 50 * '-')
print(sdk.protocol_details)
print(122 * '-')

device = sdk.get_devices()
device_count = len(device)
print('Devices Found:', device_count)
i = 0
for _ in device:
    print('    ', i, _)
    i += 1
print(122 * '-')

# Enumerate
i_0 = 0
for devices in device:

    # 0 Device Name
    i_str = str(i_0)

    key_name = []
    key_id = []
    key_color = []
    key_pos = []

    # 1. Get Key Names & Key IDs
    led_position = sdk.get_led_positions_by_device_index(i_0)
    led_position_str = str(led_position).split('), ')
    for _ in led_position_str:
        var = _.split()
        # print(var)
        var_0 = var[0]
        var_0 = var_0.replace('{', '')
        var_0 = var_0.replace('<', '')
        var_0 = var_0.replace(':', '')
        var_1 = var[1].replace('>:', '')
        var_2 = var[2].replace('(', '')
        var_2 = var_2.replace('{', '')
        var_3 = var[3].replace(')', '')
        var_3 = var_3.replace('}', '')
        key_name.append(var_0)
        key_id.append(int(var_1))
        key_pos.append(str(var_2+var_3))

    # 2. Use Key ID List To Get Key Colors
    led_color = sdk.get_led_colors_by_device_index(i_0, key_id)
    led_position_str = str(led_color).split('), ')
    for _ in led_position_str:
        var = _.split(':')
        var_color = var[2]
        var_color = var_color.replace('(', '')
        var_color = var_color.replace(')', '')
        var_color = var_color.replace('}', '')
        key_color.append(var_color)

    device_str_max = max(len(str(ele)) for ele in device)
    key_name_max_str = max(len(str(ele)) for ele in key_name)
    key_id_max_str = max(len(str(ele)) for ele in key_id)
    key_color_max_str = max(len(str(ele)) for ele in key_color)

    # 3. Print Enumerated Data
    print('')
    print(122 * '-')
    print('[DEVICE NAME]', (' ' * (device_str_max - 10)), '[CORSAIR LED ID]', (' ' * (key_name_max_str - 14)), '[LED ID]', (' ' * (key_id_max_str - 1)), '[RGB]', (' ' * (key_color_max_str - 4)), '[POSITION]')
    print(122 * '-')
    print(i_0, device[i_0])
    i = 0
    for _ in key_name:
        key_id_str = str(key_id[i])
        key_color_str = str(key_color[i])
        print(' ' * (device_str_max + 4), _, (' ' * (key_name_max_str - len(_) + 2)), key_id[i], (' ' * (key_id_max_str - len(key_id_str) + 6)), key_color[i], (' ' * (key_color_max_str - len(key_color_str) + 2)), key_pos[i])
        i += 1

    print(122 * '-')
    i_0 += 1

input('\nPress Any Key To Quit')

