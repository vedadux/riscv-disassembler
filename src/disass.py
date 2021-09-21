# coding: utf-8

from ctypes import *
import os

THIS_DIR = os.path.dirname(os.path.realpath(__file__))
LIB_DIR = "/".join(THIS_DIR.split("/")[:-1]) + "/build"
LIB_PATH = LIB_DIR + "/librvasm.so"
BUFF_LEN = 100
RV32_ISA = c_int(0)

funs = CDLL(LIB_PATH)


def disassemble(instr):
    buff = c_buffer(b"", BUFF_LEN)
    bufflen = c_size_t(BUFF_LEN)
    pc = c_uint64(0)
    rv_instr = c_uint64(instr)
    res = funs.disasm_inst(buff, bufflen, RV32_ISA, pc, rv_instr)
    assert(res == 0)
    epos = buff.raw.find(b"\0")
    disass_text = buff.raw[:epos].decode("ascii")
    return " ".join(disass_text.split()[1:])

