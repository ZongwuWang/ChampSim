/*************************************************************************
	> File Name: parserTrace.cpp
	> Author: Wang Zongwu
	> Mail: wangzongwu@outlook.com
	> Created Time: Wed 20 Oct 2021 11:17:57 PM CST
# Description: 
 ************************************************************************/

#include <iostream>
#include <stdio.h>
#include "input_instr.h"

using namespace std;

FILE *trace_file;

char gunzip_command[1024] = "xz -dc 602.gcc_s-734B.champsimtrace.xz";

int main()
{
    input_instr trace_read_instr;
    trace_file = popen(gunzip_command, "r");
    int instr_length = sizeof(input_instr);
    cout << "Size of input_instr = " << instr_length << endl;
    cout << "Press enter to continue, and press q to quit." << endl;
    while(cin.get() != 'q')
    {
        if (!fread(&trace_read_instr, 64, 1, trace_file))
        {
            cout << "*** Reach end of trace. ***" << endl;
            pclose(trace_file);
            break;
        }
        else
        {
            cout << "input_instr.ip = " << trace_read_instr.ip \
            << ";\tis_branch = " << trace_read_instr.is_branch \
            << ";\tbranch_taken = " << trace_read_instr.branch_taken \
            << endl; 
        }
    }
    return 0;
}
