
Commands =  {
    "USER": "El campo de argumento es una cadena Telnet que identifica al usuario. La identificación del usuario es la que requiere el servidor para acceder a su sistema de archivos. Este comando será normalmente el primer comando transmitido por el usuario después de que se establezcan las conexiones de control (algunos servidores pueden requerir esto). Información adicional de identificación en forma de contraseña y/o un comando de cuenta también puede ser requerida por algunos servidores. Los servidores pueden permitir que se ingrese un nuevo comando USER en cualquier momento para cambiar el control de acceso y/o la información de contabilidad. Esto tiene el efecto de eliminar cualquier información de usuario, contraseña y cuenta ya proporcionada y comenzar de nuevo la secuencia de inicio de sesión. Todos los parámetros de transferencia permanecen sin cambios y cualquier transferencia de archivo en progreso se completa bajo los parámetros de control de acceso antiguos.",
    "PASS": "El campo de argumento es una cadena Telnet que especifica la contraseña del usuario. Este comando debe ser precedido inmediatamente por el comando de nombre de usuario y, para algunos sitios, completa la identificación del usuario para el control de acceso. Dado que la información de la contraseña es bastante sensible, en general es deseable \"enmascararla\" o suprimir su visualización. Parece que el servidor no tiene una manera infalible de lograr esto. Por lo tanto, es responsabilidad del proceso de usuario-FTP ocultar la información sensible de la contraseña.",
    "CWD": "Este comando permite al usuario trabajar con un directorio o conjunto de datos diferente para el almacenamiento o la recuperación de archivos sin alterar su información de inicio de sesión o contabilidad. Los parámetros de transferencia también permanecen sin cambios. El argumento es una ruta que especifica un directorio o un designador de grupo de archivos dependiente del sistema.",
    "SMNT": "Este comando permite al usuario montar una estructura de datos de sistema de archivos diferente sin alterar su información de inicio de sesión o contabilidad. Los parámetros de transferencia también permanecen sin cambios. El argumento es una ruta que especifica un directorio o un designador de grupo de archivos dependiente del sistema.",
    "REIN": "Este comando termina una sesión de USUARIO, eliminando toda la información de entrada/salida y de cuenta, excepto para permitir que cualquier transferencia en progreso se complete. Todos los parámetros se restablecen a la configuración predeterminada y la conexión de control permanece abierta. Esto es idéntico al estado en que se encuentra un usuario inmediatamente después de que se abre la conexión de control. Se puede esperar que un comando USER siga a continuación.",
    "QUIT": "Este comando termina una sesión de USUARIO y, si no hay una transferencia de archivos en progreso, el servidor cierra la conexión de control. Si la transferencia de archivos está en progreso, la conexión permanecerá abierta para la respuesta del resultado y luego el servidor la cerrará. Si el proceso de usuario está transfiriendo archivos para varios USUARIOS pero no desea cerrar y luego reabrir las conexiones para cada uno, entonces se debe usar el comando REIN en lugar de QUIT. Un cierre inesperado de la conexión de control hará que el servidor tome la acción efectiva de un aborto (ABOR) y una desconexión (QUIT).",
    "PORT": "El argumento es una especificación HOST-PORT para el puerto de datos que se utilizará en la conexión de datos. Existen valores predeterminados tanto para los puertos de datos del usuario como del servidor, y en circunstancias normales, este comando y su respuesta no son necesarios. Si se utiliza este comando, el argumento es la concatenación de una dirección de host de internet de 32 bits y una dirección de puerto TCP de 16 bits. Esta información de dirección se divide en campos de 8 bits y el valor de cada campo se transmite como un número decimal (en representación de cadena de caracteres). Los campos están separados por comas. Un comando de puerto sería: PORT h1,h2,h3,h4,p1,p2 donde h1 son los 8 bits de orden superior de la dirección del host de internet.",
    "PASV": "Este comando solicita al server-DTP que \"escuche\" en un puerto de datos (que no es su puerto de datos predeterminado) y que espere una conexión en lugar de iniciarla al recibir un comando de transferencia. La respuesta a este comando incluye la dirección del host y del puerto en el que el servidor está escuchando.",
    "TYPE": "El argumento especifica el tipo de representación como se describe en la Sección sobre Representación y Almacenamiento de Datos. Varios tipos requieren un segundo parámetro. El primer parámetro se denota por un solo carácter Telnet, al igual que el segundo parámetro de Formato para ASCII y EBCDIC; el segundo parámetro para byte local es un número entero decimal para indicar el tamaño de bytes. Los parámetros están separados por un <SP> (Espacio, código ASCII 32).",
    "STRU": "El argumento es un código de carácter Telnet único que especifica la estructura del archivo descrita en la Sección sobre Representación y Almacenamiento de Datos.",
    "MODE": "El argumento es un código de carácter Telnet único que especifica los modos de transferencia de datos descritos en la Sección sobre Modos de Transmisión.",
    "RETR": "Este comando hace que el servidor-DTP transfiera una copia del archivo, especificado en la ruta, al servidor-DTP o usuario-DTP en el otro extremo de la conexión de datos. El estado y el contenido del archivo en el sitio del servidor no se verán afectados.",
    "STOR": "Este comando hace que el servidor-DTP acepte los datos transferidos a través de la conexión de datos y los almacene como un archivo en el sitio del servidor. Si el archivo especificado en la ruta ya existe en el sitio del servidor, su contenido será reemplazado por los datos que se están transfiriendo. Se crea un nuevo archivo en el sitio del servidor si el archivo especificado en la ruta no existe.",
    "STOU": "Este comando se comporta como STOR, excepto que el archivo resultante se creará en el directorio actual bajo un nombre único para ese directorio. La respuesta 250 Transfer Started debe incluir el nombre generado.",
    "APPE": "Este comando hace que el servidor-DTP acepte los datos transferidos a través de la conexión de datos y los almacene en un archivo en el sitio del servidor. Si el archivo especificado en la ruta ya existe en el sitio del servidor, los datos se agregarán a ese archivo; de lo contrario, el archivo especificado en la ruta se creará en el sitio del servidor.",
    "REST": "El campo de argumento representa el marcador del servidor en el cual se debe reiniciar la transferencia de archivos. Este comando no provoca la transferencia de archivos, sino que se salta el archivo hasta el punto de control de datos especificado. Este comando debe ser seguido inmediatamente por el comando de servicio FTP apropiado que provoque la reanudación de la transferencia de archivos.",
    "RNFR": "Este comando especifica la ruta antigua del archivo que se va a renombrar. Este comando debe ser seguido inmediatamente por un comando \"renombrar a\" que especifique la nueva ruta del archivo.",
    "RNTO": "Este comando especifica la nueva ruta del archivo especificado en el comando \"renombrar desde\" inmediatamente anterior. Juntos, los dos comandos causan que se renombre un archivo.",
    "ABOR": "Este comando indica al servidor que aborte el comando de servicio FTP anterior y cualquier transferencia de datos asociada. El comando de abortar puede requerir \"acción especial\", como se discute en la Sección sobre Comandos FTP, para forzar el reconocimiento por parte del servidor. No se tomará ninguna acción si el comando anterior se ha completado (incluida la transferencia de datos). La conexión de control no debe ser cerrada por el servidor, pero la conexión de datos debe ser cerrada.",
    "DELE": "Este comando hace que el archivo especificado en la ruta sea eliminado en el sitio del servidor. Si se desea un nivel adicional de protección (como la consulta, \"¿Realmente deseas eliminar?\"), debe ser proporcionado por el proceso de usuario-FTP.",
    "RMD": "Este comando hace que el directorio especificado en la ruta sea eliminado como un directorio (si la ruta es absoluta) o como un subdirectorio del directorio de trabajo actual (si la ruta es relativa).",
    "MKD": "Este comando hace que el directorio especificado en la ruta sea creado como un directorio (si la ruta es absoluta) o como un subdirectorio del directorio de trabajo actual (si la ruta es relativa).",
    "PWD": "Este comando hace que el nombre del directorio de trabajo actual sea devuelto en la respuesta.",
    "LIST": "Este comando hace que una lista sea enviada desde el servidor al DTP pasivo. Si la ruta especifica un directorio u otro grupo de archivos, el servidor debe transferir una lista de archivos en el directorio especificado. Si la ruta especifica un archivo, el servidor debe enviar información actual sobre el archivo. Un argumento nulo implica el directorio de trabajo actual o predeterminado del usuario. La transferencia de datos se realiza a través de la conexión de datos en tipo ASCII o tipo EBCDIC. (El usuario debe asegurarse de que el TIPO sea apropiadamente ASCII o EBCDIC). Dado que la información sobre un archivo puede variar ampliamente de un sistema a otro, esta información puede ser difícil de usar automáticamente en un programa, pero puede ser bastante útil para un usuario humano.",
    "NLIST": "Este comando hace que se envíe una lista de directorios desde el servidor al sitio del usuario. La ruta debe especificar un directorio u otro descriptor de grupo de archivos específico del sistema; un argumento nulo implica el directorio actual. El servidor devolverá un flujo de nombres de archivos y ninguna otra información. Los datos se transferirán en tipo ASCII o EBCDIC sobre la conexión de datos como cadenas de rutas válidas separadas por <CRLF> o <NL>. (Nuevamente, el usuario debe asegurarse de que el TIPO sea correcto). Este comando está destinado a devolver información que puede ser utilizada por un programa para procesar automáticamente los archivos. Por ejemplo, en la implementación de una función \"obtener múltiple\".",
    "SITE": "Este comando es utilizado por el servidor para proporcionar servicios específicos de su sistema que son esenciales para la transferencia de archivos, pero no lo suficientemente universales como para ser incluidos como comandos en el protocolo. La naturaleza de estos servicios y la especificación de su sintaxis pueden ser indicadas en una respuesta al comando HELP SITE.",
    "SYST": "Este comando se utiliza para averiguar el tipo de sistema operativo en el servidor. La respuesta deberá tener como su primera palabra uno de los nombres de sistema enumerados en la versión actual del documento de Números Asignados.",
    "STAT": "Este comando hará que se envíe una respuesta de estado a través de la conexión de control en forma de una respuesta. El comando puede ser enviado durante una transferencia de archivos (junto con las señales Telnet IP y Synch; véase la Sección sobre Comandos FTP), en cuyo caso el servidor responderá con el estado de la operación en progreso, o puede ser enviado entre transferencias de archivos. En este último caso, el comando puede tener un campo de argumento. Si el argumento es una ruta, el comando es análogo al comando \"listar\", excepto que los datos se transferirán a través de la conexión de control. Si se da una ruta parcial, el servidor puede responder con una lista de nombres de archivos o atributos asociados con esa especificación. Si no se da ningún argumento, el servidor debe devolver información de estado general sobre el proceso FTP del servidor. Esto debe incluir valores actuales de todos los parámetros de transferencia y el estado de las conexiones.",
    "HELP": "Este comando hará que el servidor envíe información útil sobre su estado de implementación a través de la conexión de control al usuario. El comando puede tomar un argumento (por ejemplo, cualquier nombre de comando) y devolver información más específica como respuesta. La respuesta es de tipo 211 o 214. Se sugiere que se permita el comando HELP antes de ingresar un comando USER. El servidor puede usar esta respuesta para especificar parámetros dependientes del sitio, por ejemplo, en respuesta a HELP SITE.",
    "NOOP": "Este comando no afecta ningún parámetro ni comandos ingresados previamente. No especifica ninguna acción más allá de que el servidor envíe una respuesta de OK."
}

# Método que divide la entrada en command y arg
def recv_cmd(entry):    
    if not entry:
        return None, None
        
    cmd = entry[0].upper()
    args = ' '.join(entry[1:])  # Unir los argumentos en un solo string
        
    return cmd, args

# Método para validar argumentos
def validate_args(cmd , args):
    if not args:
        raise ValueError(f"Error: No arguments provided for the command {cmd}.")
    
# Método para validar el comando TYPE
def validate_type(ftp_type):
    if not ftp_type in "A,E,I,N,T,C,M".split(","):
        raise ValueError(f"Error: Invalid Type {ftp_type}")
    
def validate_stru(stru):
    if not stru in "F,R,P".split(","):
        raise ValueError(f"Error: Invalid Struct {stru}")
    
def validate_mode(mode):
    if not mode in "F,R,P".split(","):
        raise ValueError(f"Error: Invalid Mode {mode}")

# Calcular distancia de levenshtein
def levenshtein_distance(s1, s2):
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)
    if s1[0] == s2[0]:
        return levenshtein_distance(s1[1:], s2[1:])
    
    insert_cost = levenshtein_distance(s1, s2[1:])
    delete_cost = levenshtein_distance(s1[1:], s2)
    replace_cost = levenshtein_distance(s1[1:], s2[1:])
    
    return 1 + min(insert_cost, delete_cost, replace_cost)

# Devuelve el comando mas parecido al ingresado
def Get_suggestion(command):
    lev = 1000000000000
    sug = ""
    for c in Commands.keys:
        newLev = levenshtein_distance(c, command)
        if newLev < lev:
            lev = newLev
            sug = c
    return sug