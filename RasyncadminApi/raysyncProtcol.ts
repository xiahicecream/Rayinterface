export const Action = {
    UNKNOW: 'UNKNOW',
    PING: 'PING',           // ping
    HEART_BEAT: 'HEART_BEAT',           // 心跳

    SERVERMODE: 'servermode',

    CHECK: 'check',          // 检查客户端
    LOGIN: 'login',          // 登录
    LOGOUT: 'logout',          // 注销
    SERVERS: 'servers',          // 获取能够连接的所有server列表
    GET_FTPMODE: 'GET_FTPMODE',          // 获取ftp模式
    UPLOAD: 'upload',          // 上传
    MANUAL_TRANSFER: 'manual_transfer',
    DOWNLOAD: 'download',          // 下载
    DOWNLOADTO: 'downloadto',          // 下载到

    LS: 'list',          // 列出当前文件夹下的文件列表
    MV: 'mv',          // 移动
    RM: 'remove',          // 删除
    RN: 'rename',          // 重命名
    MKDIR: 'create_folder',          // 新建文件夹
    GET_TRANS_COUNT: 'get_trans_count', // 获取当前用户正在传输任务数
    OPEN_TRANS_LIST: 'open_trans_list', // 打开传输列表
    START_UPDATE: 'start_update',

    START: 'start',         // 启动
    RESTART: 'restart',         // 重启
    SHUTDOWN: 'shutdown',         // 关闭
    SESSIONS: 'sessions',         // 获取FTP-SERVER的全部会话
    // --------- 后台 --------
    SELECT_USER: 'SELECT_USER',         // 获取单个用户
    SELECT_USERS: 'SELECT_USERS',         // 获取全部用户
    CREATE_USER: 'CREATE_USER',         // 创建单个用户
    CREATE_USERS: 'CREATE_USERS',         // 创建用户
    DELETE_USER: 'DELETE_USER',         // 删除单个用户
    DELETE_USERS: 'DELETE_USERS',         // 删除用户
    UPDATE_USER: 'UPDATE_USER',         // 修改单个用户
    UPDATE_USERS: 'UPDATE_USERS',         // 修改用户
    USERS_COUNT: 'USERS_COUNT',         // 获取总数
    UPDATE_USERPWD: 'UPDATE_USERPWD',         // 修改密码
    UPDATE_USERPWD_WEBUI: 'UPDATE_USERPWD_WEBUI', // 用戶修改密码

    SELECT_ADMIN: 'UPDATE_USERPWD',         // 获取单个用户
    SELECT_ADMINS: 'SELECT_ADMINS',         // 获取全部用户
    CREATE_ADMIN: 'CREATE_ADMIN',         // 创建单个用户
    CREATE_ADMINS: 'CREATE_ADMINS',         // 创建用户
    DELETE_ADMINS: 'DELETE_ADMINS',         // 删除用户
    UPDATE_ADMIN: 'UPDATE_ADMIN',         // 修改单个用户
    UPDATE_ADMINS: 'UPDATE_ADMINS',         // 修改用户
    ADMINS_COUNT: 'ADMINS_COUNT',         // 获取总数
    UPDATE_ADMINPWD: 'UPDATE_ADMINPWD',         // 修改管理员密码

    SELECT_SERVER: 'SELECT_SERVER',         // 获取单个SEVER
    SELECT_SERVERS: 'SELECT_SERVERS',         // 获取全部SEVER
    CREATE_SERVER: 'CREATE_SERVER',         // 创建单个SEVER
    CREATE_SERVERS: 'CREATE_SERVERS',         // 创建SEVER
    DELETE_SERVER: 'DELETE_SERVER',         // 删除单个SERVER
    DELETE_SERVERS: 'DELETE_SERVERS',         // 删除SEVER
    UPDATE_SERVER: 'UPDATE_SERVER',         // 修改单个SEVER
    UPDATE_SERVERS: 'UPDATE_SERVERS',         // 修改SEVER
    SERVERS_COUNT: 'SERVERS_COUNT',         // 获取总数
    REMAIN_SERVERS: 'REMAIN_SERVERS',         // 获取未分配的全部SEVER


    PERFORMANCE: 'performance',			// 获取cpu, disk, netstat等性能信息
    LICENSE: 'license',         //

    CREATEURL: 'CREATEURL',           // 创建分享连接
    SETURLCONF: 'SETURLCONF',           // 设置连接权限
    GETURLINFO: 'GETURLINFO',           // 获取链接所有信息
    CHECKURL: 'CHECKURL',           // 检验分享链接是否密码访问
    CHECKPASSWD: 'CHECKPASSWD',           // 检查url密码
};
export const ActionReponse = {
    UNKNOW: 'UNKNOW',
    PING: 'PING',           // ping
    HEART_BEAT: 'HEART_BEAT',           // 心跳

    SERVERMODE: 'servermode',

    CHECK: 'check_response',          // 检查客户端
    LOGIN: 'login_response',          // 登录
    LOGOUT: 'logout_response',          // 注销
    SERVERS: 'servers_response',          // 获取能够连接的所有server列表
    GET_FTPMODE: 'GET_FTPMODE',          // 获取ftp模式
    UPLOAD: 'upload_response',          // 上传
    DOWNLOAD: 'download_response',          // 下载
    DOWNLOADTO: 'downloadto_response',          // 下载到

    LS: 'list_response',          // 列出当前文件夹下的文件列表
    MV: 'mv',          // 移动
    RM: 'remove_response',          // 删除
    RN: 'rename_response',          // 重命名
    MKDIR: 'create_folder_response',          // 新建文件夹
    GET_TRANS_COUNT: 'get_trans_count_response', // 获取当前用户正在传输任务数
    TASK_COUNT: 'task_count',
    START_UPDATE: 'start_update_response',
    UPDATE_CLIENT: 'download_update_file_response',
    DISCONNECT: 'disconnect',   // client disconnect form ftp server

    START: 'start',         // 启动
    RESTART: 'restart',         // 重启
    SHUTDOWN: 'shutdown',         // 关闭
    SESSIONS: 'sessions',         // 获取FTP-SERVER的全部会话
    // --------- 后台 --------
    SELECT_USER: 'SELECT_USER',         // 获取单个用户
    SELECT_USERS: 'SELECT_USERS',         // 获取全部用户
    CREATE_USER: 'CREATE_USER',         // 创建单个用户
    CREATE_USERS: 'CREATE_USERS',         // 创建用户
    DELETE_USER: 'DELETE_USER',         // 删除单个用户
    DELETE_USERS: 'DELETE_USERS',         // 删除用户
    UPDATE_USER: 'UPDATE_USER',         // 修改单个用户
    UPDATE_USERS: 'UPDATE_USERS',         // 修改用户
    USERS_COUNT: 'USERS_COUNT',         // 获取总数
    UPDATE_USERPWD: 'UPDATE_USERPWD',         // 修改密码

    SELECT_ADMIN: 'UPDATE_USERPWD',         // 获取单个用户
    SELECT_ADMINS: 'SELECT_ADMINS',         // 获取全部用户
    CREATE_ADMIN: 'CREATE_ADMIN',         // 创建单个用户
    CREATE_ADMINS: 'CREATE_ADMINS',         // 创建用户
    DELETE_ADMINS: 'DELETE_ADMINS',         // 删除用户
    UPDATE_ADMIN: 'UPDATE_ADMIN',         // 修改单个用户
    UPDATE_ADMINS: 'UPDATE_ADMINS',         // 修改用户
    ADMINS_COUNT: 'ADMINS_COUNT',         // 获取总数
    UPDATE_ADMINPWD: 'UPDATE_ADMINPWD',         // 修改管理员密码

    SELECT_SERVER: 'SELECT_SERVER',         // 获取单个SEVER
    SELECT_SERVERS: 'SELECT_SERVERS',         // 获取全部SEVER
    CREATE_SERVER: 'CREATE_SERVER',         // 创建单个SEVER
    CREATE_SERVERS: 'CREATE_SERVERS',         // 创建SEVER
    DELETE_SERVER: 'DELETE_SERVER',         // 删除单个SERVER
    DELETE_SERVERS: 'DELETE_SERVERS',         // 删除SEVER
    UPDATE_SERVER: 'UPDATE_SERVER',         // 修改单个SEVER
    UPDATE_SERVERS: 'UPDATE_SERVERS',         // 修改SEVER
    SERVERS_COUNT: 'SERVERS_COUNT',         // 获取总数
    REMAIN_SERVERS: 'REMAIN_SERVERS',         // 获取未分配的全部SEVER


    PERFORMANCE: 'performance',			// 获取cpu, disk, netstat等性能信息
    LICENSE: 'license',         //

    CREATEURL: 'createurl',           // 创建分享连接
    SETURLCONF: 'seturlconf',           // 设置连接权限
    GETURLINFO: 'geturkinfo',           // 获取链接所有信息
    CHECKURL: 'chechurl',           // 检验分享链接是否密码访问
    CHECKPASSWD: 'checkpasswd',           // 检查url密码
};
export const Version = {
    ProtoVersion: 1,
};
export const Module = {
    EMPTY: 'EMPTY',
    WEBSRV: 'WEBSRV',
    WEBUI: 'WEBUI',
    WEBADMIN: 'WEBADMIN',
    PROXYC: 'PROXYC',
    PROXYS: 'PROXYS',
    FTP_CLIENT: 'FTP_CLIENT',
    FTP_SERVER: 'FTP_SERVER',
    TYPHOON_CLIENT: 'TYPHOON_CLIENT',
    TYPHOON_SERVER: 'TYPHOON_SERVER'
};
export const Result = {
    OK: 0,
    WS_UNKNOW: 1000,
    WS_DBUNKNOW: 1001,
    WS_ACCOUNTINVALID: 1002,
    WS_ACCOUNTREQUIRED: 1003,
    WS_ACCOUNTDUPLICATE: 1004,
    WS_PASSWORDINVALID: 1005,
    WS_PASSWORDREQUIRED: 1006,
    WS_SERVERINVALID: 1007,
    WS_ASSIGNINVALID: 1008,
    WS_TOKENINVALID: 1009,
    WS_IDINVALID: 1010,
    WS_PBMARSHALANY: 1011,
    WS_PBMARSHAL: 1012,
    WS_PBUNMARSHAL: 1013,
    WS_EMAILDUPLICATE: 1014,
    WS_SERVERDEVICEREQUIRED: 1015,
    WS_SERVERDEVICEDUPLICATE: 1016,
    WS_ASSIGNDUPLICATE: 1017,
    WS_ACCOUNTNOTALLOWED: 1018,
    WS_ILLEGALOPERATION: 1019,
    WS_INCORRECTACCOUNTFORMAT: 1021,
    WS_INCORRECTEMAILFORMAT: 1022,
    WS_INCORRECTPASSWORDFORMAT: 1023,
    WS_INCORRECTNAMEFORMAT: 1024,
    WS_INCORRECTPHONEFORMAT: 1025,
    WS_INCORRECTHOSTFORMAT: 1026,
    WS_INVALIDPORT: 1027,
    WS_INVALIDTCPPORT: 1028,
    WS_INVALIDUDPPORT: 1029,
    WS_INVALIDBANDWIDTH: 1030,
    WS_SITEACCESSDENIED: 1031,
    WS_ONLYONEADMIN: 1032,
    WS_DIRNOTEXIST: 1033,
    WS_FILENOTEXIST: 1034,
    WS_CMDFAILD: 1035,
    WS_INVALIDPACKAGESIZE: 1036,
    WS_DOESNOTEXIST: 1037,
    WS_INCORRECTLICENSEFORMAT: 1038,
    WS_CREATEUSERERROR: 1039,
    WS_NOTFOUNDNETCARD: 1040,
    WS_URLBROKEN: 1041,
    WS_NOPERMISSION: 1042,
    WS_PATHNOTEXIST: 1043,
    WS_NOREADPERMISSION: 1044,
    WS_NOWRITEPERMISSION: 1045,
    WS_ILLEGAL: 1046,          // illegal request
    WS_InvalidServerEmailAccount: 1047,         // invalid server email account
    WS_InvalidServerEmailPassword: 1048,         // invalid server email password
    WS_InvalidSmtpHostOrPort: 1049,             // invalid smtp host or port
    WS_AccountLocked: 1050,            // invalid smtp host or port
    WS_UnlockFailed: 1051,            // 解锁失败
    FC_UNKNOW: 2000,
    FC_FTPLOGIN: 2001,
    FC_FTPLIST: 2002,
    FC_FTPSERVERCLOSED: 2003,
    FC_FTPSERVERNORUN: 2004,
    FC_FTPSERVERDISC: 2005,
    FC_OTHERUSERLOGIN: 2006,
    FC_DIRNOTEXIST: 2007,
    FC_FTPLOGING: 2008,
    FC_CONNECTFAILD: 2009,
    FC_MKDNOPERMISSION: 2010,
    FC_CWDNOPERMISSION: 2011,
    FC_RECONNECT: 2012,
    FC_FTPCLIENTDISC: 2013,
    FC_PARAMERR: 2014,
    FC_AUTHFAILED: 2015,
    FC_UPLOADRECURSIVING: 2016,

    ERROR_PROXY_TIMEOUT: 30000,		// 代理服务器连接超时
    ERROR_CLIENT_CLOSED: 30001,				// 客户端连接断开
    ERROR_CLIENT_TIMEOUT: 30002,				// 客户端处理超时
    ERROR_MANAGER_ERROR: 30003,				// 管理器内部错误
    ERROR_NOT_LOGIN_INFO: 30004,				// 客户端未登录，可能客户端崩溃后正在登录或登录失败，或Web在未登录时发送需要登录才能处理的命令
    ERROR_FAILED_TO_START_PROGRM: 30005        // failed start update client;

};
export const FileType = {
    FILE: 0,
    DIRECTORY: 1,
    SYMLINK_FILE: 2,
    SYMLINK_DIRECTORY: 3,
    SYMLINK_UNKNOWN: 4,
    IS_DIR: true,
};

export const FileDialogType = {
    // NONE: 0,
    // FILE: 1,
    // DIRECTORY: 2,
    FILES: 0,
    DIRECTORIES: 1,
    // ANY: 5
};
