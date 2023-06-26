import random
from datetime import date, timedelta

usuarios = [ 
'username',
'ieczznsg',
'kdeyaxpl',
'wdkhjtlg',
'uehwegrg',
'cdvfessk',
'csolaaiz',
'kcuyjqgc',
'oavputyr',
'ysoqmxcm',
'vsphfylj',
'lvvnxcns',
'ubqyzsby',
'wndavcrm',
'kexanhmt',
'zjxlrszh',
'dkimczkf',
'npvhzbbo',
'lzlhihsx',
'snducjrv',
'ifgaljua',
'clwnwjlc',
'sjuemihj',
'yhutfezm',
'rwxhorwo',
'fyualmnr',
'dxkwwobo',
'xaqpjkbc',
'dlmzwpux',
'fecvohcz',
'urfajpmy',
'jlqjxlln',
'nlgwuuus',
'tdlsdnnv',
'sdyojhvi',
'duivrfas',
'vtdtblmp',
'hmmsmkhf',
'nmyonnge',
'wknrhvdt',
'ihpznjsp',
'kdpzjnfp',
'lyvgoikd',
'maqwaolf',
'xtsnjjdd',
'vhfvlxix',
'flxvngcm',
'thduerxa',
'fiswgszr',
'ietzukci',
'lryiiige',
'wnukyhrf',
'ueomodha',
'bbujfvow',
'vmynltcw',
'nfaqcdua',
'qvwmdwlw',
'goypwgns',
'hzglmety',
'ultjiwaf',
'jqgogdbr',
'akbdofml',
'zolvsent',
'xuexujhy',
'myknayxf',
'mzefteyq',
'zhbsklcn',
'afhwimlq',
'qsxzakna',
'rtummizz',
'mbchcbzf',
'cxlgwqws',
'nljdkcuq',
'epmqftrw',
'iuvhdzvi',
'sywuhzog',
'iuqscrjh',
'aleuhsta',
'liuwwfha',
'neaghfqo',
'fxllngxu',
'yvngyopl',
'rhdsptcj',
'mxvjsjzu',
'zrweecwh',
'rxxjgaxh',
'ixwmtgla',
'dgrtpekv',
'ipxogxeu',
'wtzbobuu',
'rgnfqmhl',
'ffwtsuqk',
'ozrflffr',
'wkvzvjhv',
'addzdsxh',
'jhingjxd',
'hivnekiu',
'zqorpblf',
'kfzitxkv',
'vbphjtpz',
'iezmxagf',
'lqhzqckb',
'lclutdrl',
'smiapnvo',
'ohwnsajm',
'gvndtvjn',
'lsvncqui',
'atstfenu',
'kqtgwadr',
'xlbyupek',
'rqoukqnm',
'dtwiiepc',
'kfwsioac',
'gbwjmvbc',
'rjmgvffe',
'boftulha',
'djsmshev',
'zssfosmb',
'jfeoqxdh',
'jidrcxix',
'zwdajryk',
'akwyyhxx',
'cpofqzve',
'nzrzqbzo',
'bomtrgvw',
'hmyubpkv',
'jmjsehhr',
'bjqsgeqv',
'sedqaupb',
'cedqnscw',
'iokhpgrn',
'gewrqjvi',
'hxgtnfop',
'sgexohmd',
'zutukqur',
'xpsjznyk',
'chkqawhu',
'dqtwirsl',
'deqnibww',
'qjfktjop',
'ehmnqmlk',
'qwltpnci',
'mxusrjbm',
'ggmnfjwd',
'jylnmxei',
'tspzmcyp',
'xburpqrh',
'tvhgxgol',
'zyfjhjyy',
'omcdnhpx',
'vckkhhav',
'enujtldf',
'kdzmprta',
'gmtptgye',
'fgdtzhvw',
'tqzwgbno',
'vibawqbg',
'somhbwaj',
'njtdbzgi',
'oellmwnx',
'auaxajvi',
'cdywhcod',
'kpdpietj',
'putvncgt',
'qqjhfztu',
'zwxdbwff',
'gtjibefe',
'otbxwntb',
'gaetrphq',
'dgonjxva',
'pgkgnsir',
'jfpqhfnz',
'dvlwjfuq',
'srjpzhud',
'wonjzlfj',
'csucjglb',
'vzpigtsw',
'bakfhvry',
'oangkugh',
'jedkkgdi',
'qtrydqnh',
'kmsqdhdy',
'kxmyttdb',
'oeluuqql',
'hrmuloub',
'bmijmbhy',
'lbrwhvxk',
'ldhajlem',
'qmuwfaan',
'adzrbjow',
'wfrbcvmb',
'mbtxjwba',
'ubsvglat',
'ikqwjdrl',
'rxalteka',
'aisoqmxv',
'fpbuitae',
'heewrsrf',
'sgdzhwmt',
'pwubnvcp',
'bsfrnzmo',
'gsanyvxx',
'mileqdhz',
'mirscoks',
'rcgscxqi',
'rcxnjsdy',
'pffeqwoa',
'cdrqyyyi',
'hyrkhxch',
'iajegwjh',
'ieqdghku',
'cikzzovo',
'wmkrntco',
'aolgwpfp',
'hbehsomz',
'fjpssiqp',
'ztznpqny',
'wmdoqcsu',
'eqibnpgj',
'gyrgehwe',
'xwqklafj',
'gyvvedla',
'wrfwioij',
'pgoaqefy',
'sfbyvrbw',
'uqkitplk',
'gzezzmcs',
'awjykjyf',
'vjfvxjuh',
'ziitlyef',
'akokooer',
'xufuanrj',
'ewogrsut',
'anrhxuvt',
'uwmaabyz',
'rvpnfweo',
'twaafxwv',
'pbyaervm',
'xcxxwiah',
'ornzjpcw',
'olxxiygc',
'szshuzho',
'zweumvnc',
'fpxiqfcf',
'yofnaayu',
'xbtkosmc',
'bqoutfqu',
'sicijqjm',
'xuaqqqxs',
'iwufmwzp',
'cpiwlqtm',
'yzwtdhth',
'jivnqalk',
'otgaoslz',
'sknwwpsh',
'ljtoezlb',
'iauniqxd',
'cdydjvom',
'kwtuwdja',
'rujfzocs',
'ucewfdej',
'gavlvmhn',
'gfmijdfp',
'lhpxzpxb',
'qdvbwqau',
'dlbglnzx',
'qnbrkezc',
'qogbhzvd',
'agixiikp',
'mccxejqb',
'bngwnodv',
'ekbpjbcy',
'nnxpyuan',
'dtidbeld',
'twqdpwss',
'ueglevkg',
'uzjidcrq',
'kautlgks',
'mqfdbhjh',
'tjymdmca',
'rbntkqtt',
'rzxjxgfh',
'dpdrkqfj',
'omcvkqhy',
'skhznqkm',
'scypvfrg',
'xbslgzzu',
'tmqpveuk',
'tzmonkmr',
'ojbdazhw',
'nbducbyp',
'sqkumrgl',
'wxafuolq',
'sfbwuajh',
'xgomdoad',
'djnbakpf',
'iwctqlqb',
'ewvcpaxw',
'lpvajaae',
'sznlpmuv',
'vldujpgz',
'xphgodqy',
'uopbjgjo',
'opdcsoag',
'zhofzbzr',
'bxzesnzd',
'bindhuan',
'croqpaam',
'gffvyrry',
'iecwidia',
'ghidzirr',
'akhqoqpn',
'vaeptovd',
'bqjqliir',
'yaznnlsl',
'cqrbikhv',
'dbsuzyok',
'dsckexlp',
'tbhdsfrq',
'zqzgihwi',
'qplwgdqx',
'rbpfrcut',
'zouyayeu',
'xlteglde',
'cuvmijlb',
'ixnsdeqq',
'trbadcyu',
'hqxwqbmq',
'vdottzca',
'wphzswky',
'yaxyhufj',
'zcdzqqwo',
'gqieggyz',
'acvdrthp',
'itvzuqub',
'prsaqfle',
'xmcvgbtl',
'aynavpfb',
'qyhxhkhn',
'roikutdv',
'gdwjzazs',
'vtxipbox',
'ygzmvwxm',
'qosmcqfj',
'ekdcilcy',
'ofjybybi',
'irrkximh',
'knlovmkj',
'iubqltwh',
'qiewrowk',
'nmzcfszf',
'ixffhzdu',
'aserjrai',
'mnogivrz',
'rumhulzc',
'dzmocqvl',
'rndnuskd',
'pnouqjjw',
'houtlrfe',
'ocfxxjld',
'wqrwcglc',
'qzrxqhce',
'tpnaahuj',
'ltfrkwxn',
'tbudlhiq',
'ujugvkez',
'ptjlxizp',
'gyoxhcsh',
'ffygkers',
'hpbpholy',
'rrdrkkxp',
'xgieqhht',
'jsyxxzah',
'rwedcwtj',
'syturicf',
'ldfpzvba',
'afwqskke',
'geyljtar',
'tdosjard',
'ptjjhdne',
'zgesxcbs',
'btyfzljn',
'owztwumv',
'eioheecm',
'smwwxpvf',
'ysoofjpi',
'imkssapc',
'oljupdul',
'whgmkzwg',
'iajaqndw',
'lxzoiwnj',
'vrzzxdtw',
'vyvakqht',
'cmogxjrb',
'itankhhp',
'dahdjjwu',
'zisnyaxc',
'wzqdmbjw',
'seqenzuh',
'uvxdhast',
'cibxjlja',
'bevejubj',
'gsvctbnn',
'nrjdmxmu',
'vivyopyu',
'yamansuh',
'ewglnigq',
'etqqejtz',
'ujogrdel',
'frfjxrna',
'juzgqlso',
'ceexlemh',
'fsskxomn',
'hfhpuxfu',
'zxsrzlbc',
'jffexewg',
'orafifcq',
'oxkwnpfx',
'quxdnqpo',
'lnuhlwfs',
'cwmnrvrj',
'rpdngpkn',
'smbpjrwl',
'ymavwatc',
'bmmzcttc',
'qebonuzn',
'rlfvvlam',
'vpsbohzn',
'zxiycxwm',
'wtuookhe',
'sbowdlmi',
'ujuwkuuj',
'iormvgdk',
'rfkkhzre',
'vcbqvmpu',
'cusduejk',
'awrkvviw',
'vrkdmbts',
'bwkbihvn',
'ipixypil',
'bnatpidd',
'xhziapth',
'xjrjqqok',
'iozybtlh',
'pjelnfrq',
'ghebueay',
'waryssdx',
'vhcwhybt',
'ykkpfhxx',
'dqxqwshd',
'otyepneg',
'zqpazlar',
'dscazxbg',
'hopqdqpv',
'lkhrslte',
'wjhhbehg',
'gujuiubv',
'sqtvgjlf',
'hskswzhq',
'fklvxbch',
'qnlmihhi',
'bnsuldiv',
'bujgiwpn',
'dmrowzae',
'lwpzzxho',
'lzqerslz',
'klyimfzh',
'qwmvmrvp',
'igzeogrp',
'jihnhupc',
'ggrzxqnh',
'xswvrwhg',
'esfrcpdr',
'okxzhqsm',
'csnwjoto',
'pojlnftq',
'nawdcalo',
'rjexxaoo',
'ljqwzkvd',
'fjuiftri',
'imbbzllz',
'beahknhq',
'hmskobip',
'xpvayozl',
'gjzyjuii',
'pejepbbs',
'zphibhhs',
'jftacnmx',
'bbobqlrs',
'leefjzvh',
'daxihidw',
'fjicmkja',
'kjnhefem',
'nyoxzaej',
'vtnuwygl',
'kwlvcitc',
'roxxlenv',
'rqkscdqx',
'ilgjlryo',
'ocxbqtty',
'sopearbk',
'yzmujghl',
'thiauuev',
'gnrzxhtu',
'rmuqimya',
'xmihkomz',
'erlujgui',
'ssvqmkjz',
'uvpgzzxz',
'zwpfkqoj',
'swdoiftf',
'uedqzcpz',
'dimusyzt',
'jegsnmpd',
'vmzspobi',
'vyhsjgwv',
'leuqnmbt',
'ljkikjnl',
'qphnyorx',
'zmtyrbpu',
'lkcfrwwk',
'znwlpuht',
'ofqivopt',
'tcgbogal',
'hncjyhhf',
'tyniwzvo',
'gehzinax',
'gengkuly',
'qzpfjrfs',
'tfvmkjht',
'gttankcp',
'jcoipxnt',
'nmjbffcl',
'vuuxsifm',
'wyvqfewc',
'lzzivizu',
'swghvwuo',
'mvawvdyk',
'qledxzqw',
'kdhvxuzd',
'ozwzzkbl',
'jkyohijr',
'srpbfzkg',
'tkmkyhzn',
'wfmpfkly',
'ybdavjwt',
'znlrgtrd',
'sppynfov',
'uqdiloqs',
'zzqywuhm',
'auiizhop',
'lcmolkgm',
'sistbghi',
'frvvnrst',
'mjwyuhdd',
'qjgahbxf',
'gjydxsrx',
'xwescdwx',
'tstzzobo',
'kvntxndc',
'ggnfckmq',
'dwhozmip',
'jfmexevn',
'vmcuxxov',
'usjjycdk',
'qikznfve',
'bmcjuowm',
'jdoucdxu',
'pkextpic',
'atvcarnp',
'gqvkicqx',
'ajjfbozr',
'sxhyhljx',
'tiojivvr',
'vkcebpye',
'nhemgtcy',
'yskclayg',
'apiqywgi',
'qcmgknwp',
'ikfbzsca',
'qgesccgk',
'xpmakjdc',
'jfnjpfqx',
'jyouaclx',
'ojslsfgl',
'hfjctbot',
'qiudymdb',
'oioccofz',
'bzolobdh',
'dquyjizz',
'utcglxwo',
'zxdprgpx',
'aywgvysp',
'czhqtcgv',
'yvgresad',
'nozlquop',
'ucmevcae',
'wfzuhrgq',
'admvmeze',
'sxcclzoi',
'zsoykune',
'csnlsobo',
'srtismrg',
'ljiaanzo',
'qllawnpq',
'otpgdmrp',
'xhrtpcqx',
'gjgeiqrr',
'wnjpudbj',
'ksxmxsem',
'ouvbbcnr',
'ydbsfsww',
'eachuzvy',
'irhpcgon',
'ygcquzhe',
'igxqpqvq',
'eltqsrka',
'ouigyxpr',
'musiobdz',
'ztvskbqk',
'cpqktpxy',
'kamnogsb',
'fnozsegy',
'unuaqqwy',
'tnwlgkpy',
'yizzpkmy',
'dqbmkmxe',
'vrvhahun',
'cljxtgix',
'fmuxrbzv',
'jipdbzls',
'wjdpkfuu',
'wvfafdgq',
'ksravxfi',
'mkbuzzag',
'smvmthix',
'pskjsvfa',
'onblmass',
'znbupaei',
'fqjxcaep',
'huneolec',
'lvnsdtyc',
'zqkqjqur',
'hosxosfq',
'oxmyiocm',
'uzvgpfsv',
'yhphiizg',
'noktfinj',
'msloyoqc',
'cbhyjsfz',
'uvchjhtj',
'eaeqoeza',
'fkyackfm',
'rbyapfdn',
'ryzarqqj',
'vceealsm',
'pphikjfe',
'bzsigbpy',
'eexmsilm',
'hzkzfszv',
'sdtxjqdn',
'wybwsnlz',
'uetlrwvc',
'jpizpoqa',
'toojzjck',
'jyjwhprk',
'wvvpgnsc',
'tprdxele',
'vjbpafxs',
'wzfyskkz',
'bjpexmeo',
'medjeirw',
'sqkpopnl',
'frlkrwcm',
'crnepyjv',
'wysbmjam',
'mgegfhmt',
'xpbvbbmu',
'kxztujkm',
'ruguuxmv',
'mpjzcigd',
'rdhrhvra',
'sexcudou',
'gcwsggle',
'ddmqwusq',
'rmuveohn',
'tjpnmqht',
'oqspclsq',
'amypikdm',
'gghwuntp',
'ofblwtel',
'cygovbbx',
'lycqjrzi',
'wozuaraa',
'ymikqdsy',
'dtckwjdn',
'tnuryvyi',
'wimpafcm',
'dprfubbh',
'ymfjtsrf',
'zuxreghe',
'xtbymbou',
'dkaffnas',
'ewupbbpq',
'ldzbqcez',
'akzdzhaw',
'jdocpfir',
'thfsdhdg',
'uglhrxly',
'ypavlshw',
'wlelshzb',
'hingblud',
'jwgavcnk',
'jjizqmat',
'mzlrrije',
'seckxswa',
'xgsvgbpx',
'hvxahmeb',
'cmmbpyig',
'cmwdzkun',
'nwqtwwjs',
'tfwoyxyp',
'tjqmxwzz',
'vkzbcfxp',
'gnfwxgys',
'ijpxdozd',
'nvwbkzpp',
'bmmnmyys',
'vajrijyh',
'infnwlht',
'lrvriuhd',
'atdoeehp',
'hlzirnae',
'reljrkai',
'fjnsmvsw',
'zbsrngtw',
'atpeuslj',
'ifcmlyqr',
'nmfmtehm',
'lldlvvsn',
'lnkmdmpq',
'ufedrahu',
'ysqvgues',
'dxnasaxd',
'pwaxvymx',
'uvssdgxc',
'neptvmix',
'ajvexltb',
'ftxmltse',
'bwazcury',
'ifiqmdpl',
'nqhbqobi',
'udnldnbb',
'fnrfwfhx',
'kollpere',
'sklnbive',
'xudjtotb',
'zifqlaiz',
'cpzdpmal',
'tvcsvtoa',
'bihdpnni',
'idtqksbx',
'pcgfbiyw',
'yhwgcgto',
'dkxvexyz',
'luxifpyq',
'kistrxwu',
'woaxjxer',
'qhwpafvb',
'uktoxmxx',
'ktwlkivy',
'imrhmkve',
'ercnrbga',
'tryogemt',
'wsonqsko',
'yhuyctzn',
'bhksdnnk',
'ilvtzdlr',
'dbwvkvdz',
'jbygddac',
'pueqwucc',
'mjludcav',
'ysekodkm',
'mjdafwmb',
'szzktwjk',
'xvcjhwyo',
'rlgxbptr',
'lhllfzva',
'wzrzpsnc',
'xscgqanv',
'mudzrord',
'oeobjlnx',
'ehsbnhrw',
'qvmwxmzd',
'acrbreno',
'hyufkzgq',
'zzsaqghr',
'sethnkre',
'vcwrkirw',
'htpcilyh',
'oeawkbhw',
'bxtkdxki',
'hkrwbkkm',
'ligkhraj',
'vmaqmroa',
'zfuaqwpg',
'eaxxgbcu',
'exnlnxix',
'ghfrkhmt',
'gvjrjpey',
'iribkvhv',
'jjvbxsmp',
'pkikqhlu',
'reodavnf',
'wzndoyok',
'aqstuany',
'csuiywwv',
'nciqlgbo',
'zatabest',
'faqhxvia',
'qemygcog',
'mvjktiyi',
'cvizwkao',
'fvqaqfzh',
'umihzhbl',
'moqjmbyh',
'vmmrazey',
'qezpokyg',
'ktucuctu',
'mnyhpeqw',
'bvzaazgl',
'zxvatown',
'ezvqhsmg',
'pbmhqzlw',
'pjysejai',
'nnswetyw',
'htufpnni',
'voajfbvl',
'ulqvgotj',
'hlouztic',
'plagigcr',
'fuzpyysg',
'ndytxbyd',
'xjgvskao',
'ygeimgdo',
'jigcbann',
'vrjdwmen',
'alqvzgsi',
'enosriwm',
'fllvxezd',
'xtqigamv',
'kwinlagt',
'gaopmpue',
'oxycltcn',
'vgclvvwy',
'ipmtdehi',
'ibujbilh',
'myyqyqsw',
'ueutaqgd',
'mthquver',
'jxsbeupc',
'qocaatfj',
'usamijsx',
'uwipbnar',
'qqpxzyxc',
'wephkgeg',
'haozlxcb',
'faisvezn',
'tkifgbtr',
'snejaigk',
'vanuntde',
'vulcmlfo',
'lqiszkvq',
'vypewakj',
'atfflkre',
'lbwdueii',
'mwkcyqvj',
'lvyrpeug',
'wozcdfqc',
'tmjbgjor',
'bjpaqand',
'igcocxkf',
'tjbkzrks',
'qmgiqioa',
'pycfgvdd',
'vzksmttv',
'pwuwpcon',
'blnbxxjg',
'wskkaotw',
'ezfxpabm',
'glwadnip',
'koqcwrdu',
'yitkvkqa',
'wuysbusw',
'fsronmos',
'rrujotqd',
'xtsfsecy',
'umexpxkz',
'xugdwpiy',
'zxbjwikb',
'ceqhktqs',
'rqyzrmeo',
'uhfdnvph',
'lhnbaonj',
'lskqlczj',
'alccbhnj',
'ayxouhyx',
'lxtdnvmb',
'luyfxcbr',
'bbvzdpvr',
'jyqkssvo',
'bwqhkhln',
'idmsmlzc',
'uikutuok',
'uezflchd',
'fzivrcda',
'qabzvnpt',
'tuddjugi',
'xyroqinw',
'mgmqieax',
'zoxdjnvo',
'eogezuwx',
'wbxyohhm',
'ndpowlsf',
'ipposhpm',
'mrnzffhw',
'hwagllen',
'qfvnhbbm',
'bpamdxdm',
'ilcajybl',
'wktdiqbh',
'gbtgvsal',
'phqampgj',
'tbdnxlis',
'dbrvsfqx',
'ewvvsnok',
'xpxubnlc',
'rrayomdu',
'soallhhl',
'rjmebcle',
'goqiacvy',
'qgvkywzw',
'zriboxbj',
'jppoczxi',
'lshuyler',
'yrhroljx',
'hugiipow',
'mjcdxzvw',
'zuacxppn',
'blckgvze',
'enmnntzr',
'loasyrdh',
'mjedmgsj',
'zmtfmhno',
'ezzeirwo',
'kryouike',
'dybcpxnw',
'nkiqmzzn',
'luxhgafs',
'ahsloviv',
'jsfjmvef',
'wmcossnn',
'mteqxikn',
'oxkrymje',
'ozsvsbxj',
'gkuvinxv',
'smzpczoo',
'prnzxvkn',
'hyomltcp',
'vdhyykrg',
'vljezlsq',
'qyrvmzkz',
'clksmwwx',
'obboosfb',
'wydfetou',
'ndyuxwbj',
'ytxgefku',
'yvkvmhxe',
'hsqbuacp',
'nuxtbcsb',
'nvvzklej',
'uzeurmtu',
'vqtaziia',
'wabbjryb',
'cwfixapi',
'gelthvbj',
'mmhsvgyg',
'unkjwmvw',
'yzioyiht',
'nyjwkfhp',
'ijpzhssy',
'erkonjag',
'cthgbjzz',
'eqirucdh',
'iksthfrf',
'glhhtmcm',
'gpcekxju',
'isvqcdkx',
'twogflcv',
'oyvgujye',
'camgsvti'
]  # Exemplo de nomes de usuários

codigo_jogos = ['1',
'9',
'28',
'46',
'72',
'90',
'104',
'134',
'139',
'164',
'189',
'216',
'230',
'242',
'248',
'273',
'277',
'287',
'307',
'324',
'331',
'334',
'343',
'344',
'349',
'366',
'388',
'408',
'434',
'478',
'482',
'489',
'518',
'574',
'577',
'586',
'601',
'604',
'628',
'663',
'690',
'699',
'722',
'725',
'754',
'773',
'833',
'836',
'840',
'870',
'919',
'920',
'928',
'931',
'949',
'981',
'991',
'1000',
'1030',
'1136',
'1158',
'1229',
'1258',
'1265',
'1289',
'1373',
'1401',
'1445',
'1536',
'1560',
'1629',
'1637',
'1690',
'1701',
'1787',
'1803',
'1821',
'1822',
'1829',
'1838',
'1842',
'1848',
'1852',
'1866',
'1889',
'1966',
'1986',
'2000',
'2035',
'2082',
'2090',
'2110',
'2164',
'2174',
'2184',
'2216',
'2226',
'2278',
'2314',
'2316',
'2356',
'2359',
'2384',
'2388',
'2405',
'2426',
'2536',
'2552',
'2589',
'2595',
'2656',
'2658',
'2660',
'2693',
'2708',
'2722',
'2758',
'2763',
'2770',
'2793',
'2813',
'2819',
'2822',
'2890',
'2917',
'2932',
'2999',
'3000',
'3009',
'3022',
'3037',
'3104',
'3107',
'3128',
'3160',
'3184',
'3193',
'3194',
'3219',
'3228',
'3230',
'3269',
'3311',
'3315',
'3330',
'3333',
'3360',
'3382',
'3391',
'3394',
'3434',
'3452',
'3463',
'3483',
'3496',
'3497',
'3498',
'3517',
'3525',
'3534',
'3605',
'3607',
'3637',
'3644',
'3663',
'3696',
'3699',
'3714',
'3768',
'3781',
'3791',
'3798',
'3894',
'3935',
'3949',
'3956',
'3961',
'3979',
'4000',
'4001',
'4002',
'4042',
'4103',
'4104',
'4246',
'4350',
'4381',
'4446',
'4452',
'4458',
'4468',
'4483',
'4504',
'4514',
'4567',
'4577',
'4578',
'4623',
'4639',
'4667',
'4699',
'4700',
'4722',
'4734',
'4745',
'4752',
'4755',
'4774',
'4806',
'4844',
'4857',
'4964',
'4975',
'4980',
'4983',
'4996',
'5000',
'5053',
'5063',
'5106',
'5123',
'5159',
'5185',
'5198',
'5202',
'5219',
'5236',
'5257',
'5258',
'5401',
'5429',
'5445',
'5518',
'5551',
'5567',
'5582',
'5585',
'5589',
'5621',
'5632',
'5644',
'5666',
'5793',
'5815',
'5817',
'5833',
'5835',
'5849',
'5889',
'5955',
'5970',
'5974',
'6011',
'6012',
'6018',
'6026',
'6121',
'6127',
'6198',
'6226',
'6235',
'6246',
'6247',
'6271',
'6310',
'6339',
'6394',
'6396',
'6410',
'6411',
'6417',
'6441',
'6467',
'6488',
'6496',
'6518',
'6542',
'6547',
'6548',
'6549',
'6552',
'6558',
'6575',
'6601',
'6603',
'6613',
'6614',
'6642',
'6671',
'6680',
'6699',
'6723',
'6729',
'6739',
'6748',
'6778',
'6780',
'6785',
'6845',
'6850',
'6953',
'6994',
'7052',
'7095',
'7096',
'7206',
'7208',
'7239',
'7241',
'7309',
'7337',
'7355',
'7364',
'7380',
'7414',
'7433',
'7438',
'7465',
'7513',
'7534',
'7539',
'7549',
'7568',
'7578',
'7588',
'7605',
'7642',
'7643',
'7655',
'7670',
'7694',
'7714',
'7725',
'7734',
'7749',
'7756',
'7762',
'7776',
'7824',
'7850',
'7862',
'8044',
'8112',
'8136',
'8190',
'8233',
'8266',
'8285',
'8340',
'8351',
'8373',
'8431',
'8436',
'8437',
'8455',
'8469',
'8485',
'8497',
'8501',
'8509',
'8510',
'8516',
'8524',
'8531',
'8585',
'8586',
'8629',
'8633',
'8657',
'8703',
'8710',
'8739',
'8763',
'8764',
'8793',
'8839',
'8841',
'8843',
'8868',
'8881',
'8884',
'8887',
'8889',
'8945',
'8998',
'9007',
'9011',
'9013',
'9028',
'9105',
'9120',
'9166',
'9189',
'9192',
'9195',
'9207',
'9228',
'9243',
'9255',
'9297',
'9343',
'9345',
'9376',
'9407',
'9488',
'9510',
'9528',
'9621',
'9660',
'9699',
'9732',
'9752',
'9756',
'9821',
'9822',
'9897',
'9955',
'9979'
]
ano = random.randint(2000, 2023)
dia = random.randint(1, 28)
mes = random.randint(1, 12)
data_inicio = date(2000, 1, 1)  # Exemplo de data inicial

with open("insert_commands.txt", "w") as file:

    for _ in range(400):  # Altere o valor 10 para o número desejado de comandos de inserção
        ano = random.randint(2000, 2023)
        dia = random.randint(1, 28)
        mes = random.randint(1, 12)
        data_inicio = date(ano, mes, dia)
        usuario = random.choice(usuarios)
        #usuario = 'admvmeze'
        codigo_jogo = random.choice(codigo_jogos)
        data_aquisicao = data_inicio + timedelta(days=random.randint(0, 365))
        command = f"INSERT INTO `lista_de_desejos` VALUES ('{usuario}', {codigo_jogo}, '{data_aquisicao}');\n"
        file.write(command)
