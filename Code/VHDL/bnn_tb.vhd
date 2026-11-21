library ieee;
use ieee.std_logic_1164.all;

entity bnn_tb is
end entity;

architecture Behavioral of bnn_tb is
    component bnn_core
    end component;

begin
    -- Instantiate the BNN core
    uut: bnn_core;

    -- Simulation loop to keep Vivado simulator running
    stim_proc: process
    begin
        wait for 1 min;  -- run for 60 seconds (or use wait forever)
        report "Simulation ended after 60 seconds." severity note;
        wait;
    end process;

end architecture;
