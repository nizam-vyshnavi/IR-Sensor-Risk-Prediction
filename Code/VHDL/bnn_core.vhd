library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use std.textio.all;
use work.bnn_pkg1.all;

entity bnn_core is
end entity;

architecture Behavioral of bnn_core is
    signal inputs : int_array_10 := (others => 0);

    -- You will reopen files inside the loop
    file input_file  : text;
    file output_file : text;

    function dropout_mask(index : integer) return integer is
    begin
        return (index * 23 + 7) mod 2;
    end function;

    function relu(x : integer) return integer is
    begin
        if x < 0 then return 0; else return x; end if;
    end function;

    function dense_layer(input : int_array_10; node : integer) return integer is
        variable sum          : integer := 0;
        variable total_weight : integer := 0;
        variable weight       : integer;
    begin
        for i in 0 to 9 loop
            if dropout_mask(i) = 1 then
                weight := ((i + node + 3) mod 5 + 1);
                sum := sum + input(i) * weight;
                total_weight := total_weight + weight;
            end if;
        end loop;
        if total_weight = 0 then
            return 0;
        else
            return relu(sum / total_weight) mod 101;
        end if;
    end function;

begin
    process
        variable in_line     : line;
        variable out_line    : line;
        variable val         : integer;
        variable preds       : int_array_5 := (others => 0);
        variable prev_inputs : int_array_10 := (others => -1);
        variable changed     : boolean;
    begin
        while true loop
            -- Always reopen input file for fresh data
            file_close(input_file);
            file_open(input_file, "C:/BNN_FINAL/input.txt", read_mode);

            changed := false;

            if not endfile(input_file) then
                readline(input_file, in_line);
                for i in 0 to 9 loop
                    read(in_line, val);
                    if val /= prev_inputs(i) then
                        changed := true;
                    end if;
                    inputs(i) <= val;
                    prev_inputs(i) := val;
                end loop;
            end if;

            wait for 50 ns;

            if changed then
                for j in 0 to 4 loop
                    preds(j) := dense_layer(inputs, j);
                end loop;

                wait for 50 ns;

                -- Reopen output.txt and write updated predictions
                file_close(output_file);
                file_open(output_file, "C:/BNN_FINAL/output.txt", write_mode);

                write(out_line, preds(0)); write(out_line, string'(" "));
                write(out_line, preds(1)); write(out_line, string'(" "));
                write(out_line, preds(2)); write(out_line, string'(" "));
                write(out_line, preds(3)); write(out_line, string'(" "));
                write(out_line, preds(4));
                writeline(output_file, out_line);
            end if;

            wait for 500 ms;
        end loop;
    end process;
end architecture;
