#引入 sys 标准库
import sys

print("RECLIMIT:{}, EXEPATH:{}, UNICODE:{}".
      format(sys.getrecursionlimit(),sys.executable,sys.maxunicode))
