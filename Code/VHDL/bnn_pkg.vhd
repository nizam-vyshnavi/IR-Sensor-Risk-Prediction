library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

package bnn_pkg is
    subtype int16 is integer range -32768 to 32767;
    type int_array_10 is array (0 to 9) of int16;
    type int_array_5 is array (0 to 4) of int16;
end package;
