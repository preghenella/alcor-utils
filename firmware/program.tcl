open_hw_manager
connect_hw_server -allow_non_jtag
open_hw_target
current_hw_device [get_hw_devices xc7k325t_0]
refresh_hw_device -update_hw_probes false [lindex [get_hw_devices xctk325t_0] 0]
set_property PROBES.FILE {/home/eic/alcor/firmware/pro.ltx} [get_hw_devices xc7k325t_0]
set_property FULL_PROBES.FILE {/home/eic/alcor/firmware/pro.ltx} [get_hw_devices xc7k325t_0]
set_property PROGRAM.FILE {/home/eic/alcor/firmware/pro.bit} [get_hw_devices xc7k325t_0]
program_hw_devices [get_hw_devices xc7k325t_0]
refresh_hw_device [get_hw_devices xc7k325t_0]
