import random
from datetime import date, timedelta

usuarios = [ 
"uehwegrg",
"username",
"cdvfessk",
"oavputyr",
"ysoqmxcm",
"vsphfylj",
"lvvnxcns",
"wndavcrm",
"zjxlrszh",
"lzlhihsx",
"snducjrv",
"clwnwjlc",
"yhutfezm",
"rwxhorwo",
"fyualmnr",
"dxkwwobo",
"xaqpjkbc",
"fecvohcz",
"jlqjxlln",
"nlgwuuus",
"ihpznjsp",
"kdpzjnfp",
"lyvgoikd",
"xtsnjjdd",
"vhfvlxix",
"flxvngcm",
"thduerxa",
"lryiiige",
"nfaqcdua",
"qvwmdwlw",
"goypwgns",
"hzglmety",
"jqgogdbr",
"mzefteyq",
"zhbsklcn",
"afhwimlq",
"qsxzakna",
"mbchcbzf",
"nljdkcuq",
"iuvhdzvi",
"iuqscrjh",
"fxllngxu",
"yvngyopl",
"rhdsptcj",
"dgrtpekv",
"ipxogxeu",
"wtzbobuu",
"rgnfqmhl",
"ozrflffr",
"wkvzvjhv",
"kfzitxkv",
"lqhzqckb",
"lclutdrl",
"lsvncqui",
"kqtgwadr",
"xlbyupek",
"kfwsioac",
"gbwjmvbc",
"rjmgvffe",
"jidrcxix",
"zwdajryk",
"bomtrgvw",
"hmyubpkv",
"jmjsehhr",
"bjqsgeqv",
"sedqaupb",
"iokhpgrn",
"sgexohmd",
"deqnibww",
"qjfktjop",
"ehmnqmlk",
"mxusrjbm",
"jylnmxei",
"xburpqrh",
"zyfjhjyy",
"vckkhhav",
"enujtldf",
"oellmwnx",
"cdywhcod",
"qqjhfztu",
"gtjibefe",
"dgonjxva",
"dvlwjfuq",
"srjpzhud",
"bakfhvry",
"oangkugh",
"oeluuqql",
"bmijmbhy",
"lbrwhvxk",
"adzrbjow",
"mbtxjwba",
"sgdzhwmt",
"bsfrnzmo",
"gsanyvxx",
"rcgscxqi",
"rcxnjsdy",
"pffeqwoa",
"cdrqyyyi",
"hyrkhxch",
"iajegwjh",
"cikzzovo",
"wmkrntco",
"aolgwpfp",
"fjpssiqp",
"ztznpqny",
"wmdoqcsu",
"eqibnpgj",
"wrfwioij",
"pgoaqefy",
"uqkitplk",
"gzezzmcs",
"awjykjyf",
"akokooer",
"xufuanrj",
"ewogrsut",
"anrhxuvt",
"twaafxwv",
"pbyaervm",
"olxxiygc",
"szshuzho",
"zweumvnc",
"fpxiqfcf",
"yofnaayu",
"xbtkosmc",
"sicijqjm",
"xuaqqqxs",
"iwufmwzp",
"yzwtdhth",
"jivnqalk",
"cdydjvom",
"kwtuwdja",
"gfmijdfp",
"lhpxzpxb",
"qdvbwqau",
"agixiikp",
"bngwnodv",
"ekbpjbcy",
"dtidbeld",
"twqdpwss",
"uzjidcrq",
"mqfdbhjh",
"tjymdmca",
"rbntkqtt",
"dpdrkqfj",
"skhznqkm",
"scypvfrg",
"xbslgzzu",
"tzmonkmr",
"sqkumrgl",
"sfbwuajh",
"lpvajaae",
"vldujpgz",
"zhofzbzr",
"bxzesnzd",
"iecwidia",
"ghidzirr",
"akhqoqpn",
"bqjqliir",
"yaznnlsl",
"cqrbikhv",
"dbsuzyok",
"ixnsdeqq",
"hqxwqbmq",
"vdottzca",
"wphzswky",
"yaxyhufj",
"zcdzqqwo",
"prsaqfle",
"xmcvgbtl",
"qyhxhkhn",
"roikutdv",
"gdwjzazs",
"vtxipbox",
"ygzmvwxm",
"nmzcfszf",
"aserjrai",
"mnogivrz",
"rumhulzc",
"dzmocqvl",
"pnouqjjw",
"houtlrfe",
"qzrxqhce",
"tpnaahuj",
"ltfrkwxn",
"hpbpholy",
"rrdrkkxp",
"xgieqhht",
"rwedcwtj",
"afwqskke",
"geyljtar",
"tdosjard",
"owztwumv",
"smwwxpvf",
"whgmkzwg",
"cmogxjrb",
"itankhhp",
"zisnyaxc",
"wzqdmbjw",
"seqenzuh",
"uvxdhast",
"bevejubj",
"nrjdmxmu",
"vivyopyu",
"ewglnigq",
"frfjxrna",
"ceexlemh",
"zxsrzlbc",
"orafifcq",
"quxdnqpo",
"lnuhlwfs",
"rpdngpkn",
"ymavwatc",
"qebonuzn",
"vpsbohzn",
"zxiycxwm",
"ujuwkuuj",
"iormvgdk",
"vcbqvmpu",
"awrkvviw",
"ipixypil",
"iozybtlh",
"vhcwhybt",
"ykkpfhxx",
"zqpazlar",
"gujuiubv",
"sqtvgjlf",
"hskswzhq",
"fklvxbch",
"qnlmihhi",
"bnsuldiv",
"bujgiwpn",
"lzqerslz",
"klyimfzh",
"qwmvmrvp",
"jihnhupc",
"xswvrwhg",
"pojlnftq",
"nawdcalo",
"rjexxaoo",
"imbbzllz",
"beahknhq",
"xpvayozl",
"pejepbbs",
"jftacnmx",
"bbobqlrs",
"daxihidw",
"nyoxzaej",
"roxxlenv",
"rqkscdqx",
"ilgjlryo",
"ocxbqtty",
"sopearbk",
"yzmujghl",
"thiauuev",
"gnrzxhtu",
"zwpfkqoj",
"leuqnmbt",
"qphnyorx",
"lkcfrwwk",
"tcgbogal",
"tyniwzvo",
"qzpfjrfs",
"nmjbffcl",
"wyvqfewc",
"lzzivizu",
"swghvwuo",
"ozwzzkbl",
"srpbfzkg",
"tkmkyhzn",
"wfmpfkly",
"ybdavjwt",
"znlrgtrd",
"zzqywuhm",
"lcmolkgm",
"qjgahbxf",
"gjydxsrx",
"xwescdwx",
"kvntxndc",
"dwhozmip",
"jfmexevn",
"bmcjuowm",
"pkextpic",
"atvcarnp",
"ajjfbozr",
"sxhyhljx",
"nhemgtcy",
"yskclayg",
"apiqywgi",
"qcmgknwp",
"jyouaclx",
"ojslsfgl",
"qiudymdb",
"oioccofz",
"bzolobdh",
"dquyjizz",
"utcglxwo",
"zxdprgpx",
"aywgvysp",
"czhqtcgv",
"yvgresad",
"nozlquop",
"wfzuhrgq",
"admvmeze",
"sxcclzoi",
"ljiaanzo",
"qllawnpq",
"otpgdmrp",
"gjgeiqrr",
"wnjpudbj",
"ksxmxsem",
"ouvbbcnr",
"ydbsfsww",
"irhpcgon",
"ouigyxpr",
"musiobdz",
"cpqktpxy",
"kamnogsb",
"fnozsegy",
"dqbmkmxe",
"cljxtgix",
"jipdbzls",
"wjdpkfuu",
"ksravxfi",
"onblmass",
"huneolec",
"lvnsdtyc",
"zqkqjqur",
"oxmyiocm",
"uzvgpfsv",
"yhphiizg",
"msloyoqc",
"eaeqoeza",
"ryzarqqj",
"vceealsm",
"eexmsilm",
"hzkzfszv",
"sdtxjqdn",
"uetlrwvc",
"tprdxele",
"vjbpafxs",
"wzfyskkz",
"crnepyjv",
"kxztujkm",
"rdhrhvra",
"sexcudou",
"gcwsggle",
"ddmqwusq",
"rmuveohn",
"tjpnmqht",
"oqspclsq",
"gghwuntp",
"ofblwtel",
"lycqjrzi",
"wozuaraa",
"dprfubbh",
"zuxreghe",
"xtbymbou",
"dkaffnas",
"jdocpfir",
"uglhrxly",
"ypavlshw",
"wlelshzb",
"jwgavcnk",
"mzlrrije",
"hvxahmeb",
"cmmbpyig",
"cmwdzkun",
"tfwoyxyp",
"gnfwxgys",
"vajrijyh",
"infnwlht",
"lrvriuhd",
"atdoeehp",
"reljrkai",
"zbsrngtw",
"atpeuslj",
"nmfmtehm",
"lldlvvsn",
"lnkmdmpq",
"ufedrahu",
"uvssdgxc",
"ftxmltse",
"bwazcury",
"ifiqmdpl",
"nqhbqobi",
"udnldnbb",
"fnrfwfhx",
"zifqlaiz",
"cpzdpmal",
"idtqksbx",
"pcgfbiyw",
"dkxvexyz",
"woaxjxer",
"uktoxmxx",
"ktwlkivy",
"imrhmkve",
"ercnrbga",
"wsonqsko",
"yhuyctzn",
"dbwvkvdz",
"pueqwucc",
"szzktwjk",
"xvcjhwyo",
"rlgxbptr",
"wzrzpsnc",
"mudzrord",
"oeobjlnx",
"ehsbnhrw",
"zzsaqghr",
"vcwrkirw",
"htpcilyh",
"oeawkbhw",
"ligkhraj",
"eaxxgbcu",
"reodavnf",
"faqhxvia",
"cvizwkao",
"moqjmbyh",
"qezpokyg",
"ktucuctu",
"bvzaazgl",
"pbmhqzlw",
"pjysejai",
"voajfbvl",
"plagigcr",
"fuzpyysg",
"ygeimgdo",
"alqvzgsi",
"fllvxezd",
"xtqigamv",
"gaopmpue",
"vgclvvwy",
"myyqyqsw",
"jxsbeupc",
"wephkgeg",
"haozlxcb",
"faisvezn",
"tkifgbtr",
"vanuntde",
"lqiszkvq",
"vypewakj",
"lbwdueii",
"tmjbgjor",
"bjpaqand",
"igcocxkf",
"tjbkzrks",
"qmgiqioa",
"vzksmttv",
"blnbxxjg",
"wskkaotw",
"ezfxpabm",
"glwadnip",
"koqcwrdu",
"yitkvkqa",
"rrujotqd",
"xugdwpiy",
"ceqhktqs",
"uhfdnvph",
"lskqlczj",
"alccbhnj",
"ayxouhyx",
"luyfxcbr",
"bbvzdpvr",
"bwqhkhln",
"idmsmlzc",
"uikutuok",
"fzivrcda",
"qabzvnpt",
"mgmqieax",
"zoxdjnvo",
"eogezuwx",
"mrnzffhw",
"hwagllen",
"bpamdxdm",
"gbtgvsal",
"tbdnxlis",
"ewvvsnok",
"zriboxbj",
"zuacxppn",
"enmnntzr",
"mjedmgsj",
"ezzeirwo",
"nkiqmzzn",
"luxhgafs",
"jsfjmvef",
"wmcossnn",
"ozsvsbxj",
"smzpczoo",
"prnzxvkn",
"ytxgefku",
"yvkvmhxe",
"nuxtbcsb",
"nvvzklej",
"vqtaziia",
"cwfixapi",
"nyjwkfhp",
"ijpzhssy",
"erkonjag",
"eqirucdh",
"twogflcv",
"camgsvti"]  # Exemplo de nomes de usuários

codigo_jogos = [1, 104, 134, 277, 366, 388, 408, 586, 725, 870, 928, 1000, 1289, 1629, 1787, 1838, 1986, 2000, 2314, 2405, 2426, 2536, 2552, 2589, 2656, 2708, 2917, 3000, 3184, 3333, 3382, 3394, 3452, 3463, 3483, 3496, 3497, 3498, 3534, 3663, 3699, 3714, 3768, 3781, 3791, 4000, 4002, 4042, 4103, 4246, 4446, 4667, 4700, 4722, 4752, 4806, 4996, 5000, 5185, 5202, 5258, 5401, 5518, 5833, 5955, 6247, 6310, 6411, 6441, 6601, 6613, 6699, 6729, 6748, 6845, 7095, 7239, 7380, 7438, 7513, 7670, 7714, 7734, 7749, 7776, 8112, 8285, 8455, 8485, 8501, 8509, 8516, 8585, 8710, 8793, 8881, 8887, 8889, 9013, 9192, 9255, 9343, 9528, 9756, 9822, 9897]

ano = random.randint(2000, 2023)
dia = random.randint(1, 28)
mes = random.randint(1, 12)
data_inicio = date(2000, 1, 1)  # Exemplo de data inicial

with open("insert_commands.txt", "w") as file:

    for _ in range(20):  # Altere o valor 10 para o número desejado de comandos de inserção
        ano = random.randint(2000, 2023)
        dia = random.randint(1, 28)
        mes = random.randint(1, 12)
        data_inicio = date(ano, mes, dia)
        usuario = random.choice(usuarios)
        #usuario = 'admvmeze'
        codigo_jogo = random.choice(codigo_jogos)
        data_aquisicao = data_inicio + timedelta(days=random.randint(0, 365))
        command = f"INSERT INTO `biblioteca_de_jogos` VALUES ('{usuario}', {codigo_jogo}, '{data_aquisicao}');\n"
        file.write(command)
