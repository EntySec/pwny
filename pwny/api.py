from pwny.types import *

TERM_CLOSED = 'closed by console'
TERM_UNKNOWN = 'unknown'

PIPE_INTERACTIVE = 1 << 0

TAB_BASE = 1
PIPE_TYPE = 1

PIPE_INTERNAL = 10000
PIPE_STATIC = 20000
PIPE_DYNAMIC = 40000

API_CALL = 1
API_TYPE = 1

API_CALL_INTERNAL = 10000
API_CALL_STATIC = 20000
API_CALL_DYNAMIC = 40000

ALGO = {
    0: 'No TLS enabled (!)',
    1: 'AES-CBC 256-bit (TLS v1.3)'
}

TAB_TERM = tlv_custom_tag(API_CALL_INTERNAL, TAB_BASE + 1, API_CALL)

PIPE_BASE = 1

PIPE_TYPE_TYPE = tlv_custom_type(TLV_TYPE_INT, PIPE_BASE, API_TYPE)
PIPE_TYPE_ID = tlv_custom_type(TLV_TYPE_INT, PIPE_BASE, API_TYPE + 1)
PIPE_TYPE_LENGTH = tlv_custom_type(TLV_TYPE_INT, PIPE_BASE, API_TYPE + 2)
PIPE_TYPE_BUFFER = tlv_custom_type(TLV_TYPE_BYTES, PIPE_BASE, API_TYPE)
PIPE_TYPE_OFFSET = tlv_custom_type(TLV_TYPE_INT, PIPE_BASE, API_TYPE + 3)
PIPE_TYPE_WHENCE = tlv_custom_type(TLV_TYPE_INT, PIPE_BASE, API_TYPE + 4)
PIPE_TYPE_HEARTBEAT = tlv_custom_type(TLV_TYPE_INT, PIPE_BASE, API_TYPE + 5)
PIPE_TYPE_FLAGS = tlv_custom_type(TLV_TYPE_INT, PIPE_BASE, API_TYPE + 6)

PIPE_READ = tlv_custom_tag(API_CALL_INTERNAL, PIPE_BASE, API_CALL)
PIPE_WRITE = tlv_custom_tag(API_CALL_INTERNAL, PIPE_BASE, API_CALL + 1)
PIPE_SEEK = tlv_custom_tag(API_CALL_INTERNAL, PIPE_BASE, API_CALL + 2)
PIPE_TELL = tlv_custom_tag(API_CALL_INTERNAL, PIPE_BASE, API_CALL + 3)
PIPE_CREATE = tlv_custom_tag(API_CALL_INTERNAL, PIPE_BASE, API_CALL + 4)
PIPE_DESTROY = tlv_custom_tag(API_CALL_INTERNAL, PIPE_BASE, API_CALL + 5)
PIPE_HEARTBEAT = tlv_custom_tag(API_CALL_INTERNAL, PIPE_BASE, API_CALL + 6)

BUILTIN_BASE = 1

BUILTIN_TYPE_PLATFORM = tlv_custom_type(TLV_TYPE_STRING, BUILTIN_BASE, API_TYPE)
BUILTIN_TYPE_VERSION = tlv_custom_type(TLV_TYPE_STRING, BUILTIN_BASE, API_TYPE + 1)
BUILTIN_TYPE_ARCH = tlv_custom_type(TLV_TYPE_STRING, BUILTIN_BASE, API_TYPE + 2)
BUILTIN_TYPE_MACHINE = tlv_custom_type(TLV_TYPE_STRING, BUILTIN_BASE, API_TYPE + 3)
BUILTIN_TYPE_VENDOR = tlv_custom_type(TLV_TYPE_STRING, BUILTIN_BASE, API_TYPE + 4)

BUILTIN_TYPE_RAM_USED = tlv_custom_type(TLV_TYPE_INT, BUILTIN_BASE, API_TYPE)
BUILTIN_TYPE_RAM_TOTAL = tlv_custom_type(TLV_TYPE_INT, BUILTIN_BASE, API_TYPE + 1)

BUILTIN_TYPE_PUBLIC_KEY = tlv_custom_type(TLV_TYPE_BYTES, BUILTIN_BASE, API_TYPE)
BUILTIN_TYPE_KEY = tlv_custom_type(TLV_TYPE_BYTES, BUILTIN_BASE, API_TYPE + 1)

BUILTIN_QUIT = tlv_custom_tag(API_CALL_STATIC, BUILTIN_BASE, API_CALL)
BUILTIN_ADD_TAB_DISK = tlv_custom_tag(API_CALL_STATIC, BUILTIN_BASE, API_CALL + 1)
BUILTIN_ADD_TAB_BUFFER = tlv_custom_tag(API_CALL_STATIC, BUILTIN_BASE, API_CALL + 2)
BUILTIN_DEL_TAB = tlv_custom_tag(API_CALL_STATIC, BUILTIN_BASE, API_CALL + 3)
BUILTIN_SYSINFO = tlv_custom_tag(API_CALL_STATIC, BUILTIN_BASE, API_CALL + 4)
BUILTIN_TIME = tlv_custom_tag(API_CALL_STATIC, BUILTIN_BASE, API_CALL + 5)
BUILTIN_WHOAMI = tlv_custom_tag(API_CALL_STATIC, BUILTIN_BASE, API_CALL + 6)
BUILTIN_UUID = tlv_custom_tag(API_CALL_STATIC, BUILTIN_BASE, API_CALL + 7)
BUILTIN_SECURE = tlv_custom_tag(API_CALL_STATIC, BUILTIN_BASE, API_CALL + 8)

PROCESS_BASE = 2

PROCESS_TYPE_PID_NAME = tlv_custom_type(TLV_TYPE_STRING, PROCESS_BASE, API_TYPE)
PROCESS_TYPE_PID_CPU = tlv_custom_type(TLV_TYPE_STRING, PROCESS_BASE, API_TYPE + 1)
PROCESS_TYPE_PID_PATH = tlv_custom_type(TLV_TYPE_STRING, PROCESS_BASE, API_TYPE + 2)
PROCESS_TYPE_PROCESS_ARGV = tlv_custom_type(TLV_TYPE_STRING, PROCESS_BASE, API_TYPE + 3)
PROCESS_TYPE_PROCESS_ENV = tlv_custom_type(TLV_TYPE_STRING, PROCESS_BASE, API_TYPE + 4)

PROCESS_LIST = tlv_custom_tag(API_CALL_STATIC, PROCESS_BASE, API_CALL)
PROCESS_KILL = tlv_custom_tag(API_CALL_STATIC, PROCESS_BASE, API_CALL + 1)
PROCESS_GET_PID = tlv_custom_tag(API_CALL_STATIC, PROCESS_BASE, API_CALL + 2)
PROCESS_MIGRATE = tlv_custom_tag(API_CALL_STATIC, PROCESS_BASE, API_CALL + 3)
PROCESS_KILLALL = tlv_custom_tag(API_CALL_STATIC, PROCESS_BASE, API_CALL + 4)

PROCESS_PIPE = tlv_custom_pipe(PIPE_STATIC, PROCESS_BASE, PIPE_TYPE)

FS_BASE = 3

FS_TYPE_MODE = tlv_custom_type(TLV_TYPE_STRING, FS_BASE, PIPE_TYPE)

FS_LIST = tlv_custom_tag(API_CALL_STATIC, FS_BASE, API_CALL)
FS_STAT = tlv_custom_tag(API_CALL_STATIC, FS_BASE, API_CALL + 1)
FS_GETWD = tlv_custom_tag(API_CALL_STATIC, FS_BASE, API_CALL + 2)
FS_MKDIR = tlv_custom_tag(API_CALL_STATIC, FS_BASE, API_CALL + 3)
FS_CHMOD = tlv_custom_tag(API_CALL_STATIC, FS_BASE, API_CALL + 4)
FS_CHDIR = tlv_custom_tag(API_CALL_STATIC, FS_BASE, API_CALL + 5)
FS_FILE_DELETE = tlv_custom_tag(API_CALL_STATIC, FS_BASE, API_CALL + 6)
FS_FILE_COPY = tlv_custom_tag(API_CALL_STATIC, FS_BASE, API_CALL + 7)
FS_FILE_MOVE = tlv_custom_tag(API_CALL_STATIC, FS_BASE, API_CALL + 8)
FS_DIR_DELETE = tlv_custom_tag(API_CALL_STATIC, FS_BASE, API_CALL + 9)

FS_PIPE_FILE = tlv_custom_pipe(PIPE_STATIC, FS_BASE, PIPE_TYPE)

NET_BASE = 4

NET_TYPE_URI = tlv_custom_type(TLV_TYPE_STRING, NET_BASE, API_TYPE)
NET_TYPE_ALGO = tlv_custom_type(TLV_TYPE_INT, NET_BASE, API_TYPE)
NET_TYPE_ID = tlv_custom_type(TLV_TYPE_INT, NET_BASE, API_TYPE + 1)
NET_TYPE_DELAY = tlv_custom_type(TLV_TYPE_INT, NET_BASE, API_TYPE + 2)
NET_TYPE_KEEP_ALIVE = tlv_custom_type(TLV_TYPE_INT, NET_BASE, API_TYPE + 3)

NET_TUNNELS = tlv_custom_tag(API_CALL_STATIC, NET_BASE, API_CALL)
NET_ADD_TUNNEL = tlv_custom_tag(API_CALL_STATIC, NET_BASE, API_CALL + 1)
NET_SUSPEND_TUNNEL = tlv_custom_tag(API_CALL_STATIC, NET_BASE, API_CALL + 2)
NET_ACTIVATE_TUNNEL = tlv_custom_tag(API_CALL_STATIC, NET_BASE, API_CALL + 3)
NET_RESTART_TUNNEL = tlv_custom_tag(API_CALL_STATIC, NET_BASE, API_CALL + 4)

NET_PIPE_CLIENT = tlv_custom_pipe(PIPE_STATIC, NET_BASE, PIPE_TYPE)
