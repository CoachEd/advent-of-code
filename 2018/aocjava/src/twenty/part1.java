package twenty;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Stack;

import utils.Dijkstra;
import utils.Edge1;
import utils.Vertex;

public class part1 {

	/*
	 * GUESSES: 584 (too low)
	 */

	public static int width = 289;
	public static int height = 205;
	public static int startx = 149;
	public static int starty = 107;
	public static String smap = "^EEEESWSWWN(E|WWNWNWWSESESSSWSWNNN(ESNW|)WN(E|WWNEENWNWSWSSSEESWSWWSSWWSSEEEEENNE(SESSSESESWWSESSENNESSSWWSSWWNNE(S|NNWWS(WNNEENN(NN(N|WWWSWNWSSSENES(SSSWSWSSESEENE(SEEESWSSSWSSWWSWSESSWWWSSSSEENENEEENWW(WWSW(N|S)|NNNNEEEEEESSWSEEESSWWWWN(W(SSWSESENNESSSEESESWWWWN(NWWWSSENESSSWNWWSWWWWNWNNWSWSWNWNWNENWWNWNWSSESESWSWWWNNNWNWNWNEEES(SE(SSESWENWNN|)NNNWNWNWNNNESES(W|EESEENNW(WWNWNNEENEEENNWWNWNWSWNWNWSSWNWWNNESENNEES(W|ENNNNWSSWWNNWWNEENWNNNNNENENENESSEEESSSSSENEENNNNNNESSESE(NENWNNNESSEE(NNNW(SS|WNWNWSS(WNNWWSSE(N|SES(E(SS|N)|WWWSESSW(NWWNW(NNWWS(E|WNWNNWNNESEEESS(WNWSNESE|)EEEE(NWWNNNEENWNNNNEENWWWSWSSSE(SWWWSS(WNWWNWWNWSWWWNENWWSWNNENEEEESEEEESS(WNW(S|WWW(NWWEES|)S)|SENENWNEE(NWNNNNEENNESENNNNNWWWNWNWWNWNWWNNNEESENNWWNNEENEESWS(SESWSSW(WWNSEE|)SEES(W|ESENNNENWW(NNN(W|ENWNENEESSW(SSS(WNSE|)ESSEEEEEENNWSWNWNEEENWNENNNNNEEENNNNNWSSSSWNWWNNNWNWWSSE(N|SWSEE(SSE(NEWS|)SSSWS(SSWWNW(SWSEESS(WNSE|)E|NNESE(S|NNN(ESNW|)WNENWWSWWWWWSSE(NEEEES(E|WWW)|SWWWWSWWWNNNWNEEENESSEE(NNW(NEESEEENWWNENNNNWNNESESSENNEEEES(ESESE(SSWNSENN|)NNWNNW(NWWWS(WWWNWWWSWSESWWSESWWNNWNEENNNE(EEEENNNEESWSEEEENWWNENNENWWSWWN(E|WSS(EEE|WWNN(ESNW|)WSWNWWSWSWNWWSWSESWWWNENNN(E(EEEE|S)|WWSS(ENSW|)SWSSWNWSSWWSESWWWNNWWSESSWNWSSESWWWWWSWSSESEEEESWSWNWSSSSESWSSWWNENNWNNW(NNN(ESES(W|SS)|NNNNENENESENE(NWNNWWNWNW(SSESS(EENWESWW|)SW(S|NN)|NNNEN(W|ESENESEESENN(WW|ESESSW(N|SES(E(EENNNESENNN(ESSNNW|)WSWNWW(W|SSE(SWSEWNEN|)N)|SS)|WWWNWWW(SEESSEN(SWNNWWEESSEN|)|WNN(WSNE|)ESENESEES(NWWNWSNESEES|)))))))|S))|SSS(E|SSSESESENN(W|EESWSEENESENEEENENENESESENENNWW(SEWN|)NWWNEEEES(W|EEN(ESSWSW(N|SEESWWWSWWWNWSSEESWWWN(WWSSWWN(ENSW|)WSSSSENNESSSWSEENEENEEEENENEEEE(SWSEENE(NWES|)SE(ESE(ESWSEENEESWS(WSSWWNN(ESNW|)WWWNNWN(EESSEN|WSSWSSEE(ESEE(NWES|)SESWWSESE(N|SWWWWNNNWNWSSESWWNNNN(WNWWSWSWNNWNWNW(WWSSWWNWWSWSWNNENNESEE(ESNW|)NNW(WNNWWSESWSSWSWNW(NEENWNW(NENWNEN(WN(N|E)|ESS(EEENWWNEEESSSS(NNNNWWEESSSS|)|SS))|S)|SSSEE(NWES|)SEEESENN(N|EEESEENE(NWW(NEWS|)S|ESWSSWWWWN(NWSSSSWSEENNESENESEEN(NNEESSE(SWW(NN|SSSE(NN|SSWNWSWNNENWN(WSWSESWSESEEESWSWWSEEEESSEESWSWNWWWWSSWSWSWWSEESSSWNWN(E|WWWWWWSW(SESWSEEEESSWWN(WSSSEESENN(EEEESESWWSWW(SSSSSWWNWNNEE(NNWWS(WSSSW(NNNNN(E(E|S)|NNNN)|SEESWSEEEEN(EESWSSEEENENENNWWW(WWNNESEEENNNWW(S(WNWS|ESW)|NEEESEESWWSEESW(SSENEESWSSSSWSWWSWNWWSSE(SEEN(W|ENEENESENNWNNEN(NNEENNEEESWSESWW(WSSW(S(ESENNNEESWSSENESENNEE(NNENWWNNN(EEE(N|SES(W(WNWSNESE|)SS|ENE(NWWEES|)EE))|WN(WS(WNNNE(NWNNNWWSESWWWWWWSSENEESSW(N|WW(SEESE(SWWW(NE|SEEE)|NEES(W|ENNWWNNEESW(ENWWSSNNEESW|)))|WNNNNWSWNWS(SEES(WW|S)|WNWWWWNNNNWN(WWSES(W|E)|EESESSW(SEENESEENWN(WW|EEESENEEESE(NNENENESENNWNWSWNNNNNEENNENNWSWNNENN(EESWSESSSSSSE(SWSW(WWNEN(E(NN|S)|W)|SESSSSWWSS(WWNENSWSEE|)E(N|SEESSWNWS(NESENNSSWNWS|)))|NN(ES(E|S)|NN))|WWWSE(SWSESSESWW(NNWSWNNW(NEE(S|NW(NENWESWS|)W)|W)|SSWSWWSWWSWN(WSSESENESENEENE(SS(SWNWSWS(EE|WNWWWS(WNN(E|NN)|EE))|E)|N(WWSWWEENEE|)N)|NNESEN))|E))|SWS(WNW(NEWS|)W(WWN|SE)|E)))|N)))))|S)|SESWSESS(ENSW|)W(S|N))|E))|SWSSS(EN(ESEWNW|)N|WWSESWWSESSEEEN(WN(WSNE|)(E|NN)|ESESSWSSENESSSSSEEEEESENNWNENN(ESESSSW(NN|SEENEENENWWN(EEEEESSWW(NEWS|)SEESWSEESS(EENWNNWNNNN(N|EEEEENWN(WSNE|)EESEEN(NEESWSSSEEENNW(WSEWNE|)NENESSSSSSESWSSWNWWNNN(WWWSWNN(NEESWENWWS|)WWWSSW(SSESENEESES(EEN(NW(WN(EENWESWW|)WWW(NNESNWSS|)W|S)|EES(EEENESENESEEEEEEENNWWNNESEENWNWNNWNNEEEENEEESWSW(N|SESSWW(SSSSS(WNNSSE|)EENWNNESESES(EENNESSENESEEEEENNEEEEESWS(WNWWSE|EENNNWWWWWNWNWWWNWNENEENWNNEES(ENENWWNWNEEEENNESESWSSESESESESSSENNNEENENNENWWNWNNEENWWWWNWWNEEESEENWNENNENEENWNWWS(E|SWWNWSWSSES(ENN(ESNW|)W|WWNWWNEENWWNEEENWNEEEE(S(WW|S)|NWWNENEENWNENWNEENWWWNNWNEESES(ENNENENNE(SSSSSWN(N|WSSSSSENNE(NWES|)SSSWWW(NN|SEEESSWS(WNWW(SEWN|)N(EEE|W)|SE(SSSWSW(SSS(WNNNSSSE|)ENNE(SSSWSSS(E(SWSSSW(N|SWSEESE(NN(NNN|W)|SSSWSWWNENENWWWN(W(NEWS|)SSWWWWWS(WNWNWW(SESEWNWN|)NEENESSENNE(SSENNSSWNN|)NWWN(E|W(N(NNWWEESS|)E|SW(N|SWNWSSSWNWS(NESENNSSWNWS|))))|EESSEESEES(EENEE(SWEN|)N(N|WWW(WWNWN(WSNE|)EE(NEWS|)S|S))|WWWNWS))|EE)))|NN)|WWN(ENNSSW|)W)|N)|N)|N))))|NWWSSWSW(NNNNE(NENEE(SWS(E|W)|NNWWNENE(NNNNNWWSWNNEEENNNNNWSSSWS(WNNENWNENENNWWS(SWNNNNNWWSWNWSSWSSWWNENWNWWNWSWWWSWWNWWWSSWSSESEENNN(W(NEWS|)S(S|W)|ESESESWSW(WWWWSSWWWWWNNNNWWSSWWSSWWSWNWNEEENNWWNWWSS(SSSWNNNNWWNNNWSSSSESWWWWSSSWWWNENNNNNNNNWWNENWNENWNEESESWSEESSSSEE(NWNNNEEENWNWNWW(SSE(N|E)|NNNNNWSWNNWWWSEESSSENESS(WWWNNNWSWSWSEE(N|SSWSSE(SSSSSSWNNWNENWN(E|NNNN(E|WNNNENNNNWWWSEESSWNWWNNWNWSSSWNNWWSESWSESWW(SWNWWWWWWSW(N|SS(W|ENEEN(W|ESENESESESSSSSWWWSSESSSSESSWSWNN(E|W(WWSES(W|SE(ESEEES(WWWWNWSWSWN(SENENEWSWSWN|)|ENEENWWWN(WSWENE|)NENWNEEENNESEEENENWWNNNNESSSEE(NWNNE(NNNWNNNWWNWWN(WSSWSESENE(NWES|)EESSSS(ENSW|)WWNWSWNWW(SSSSSSE(SWWW(SEEEWWWN|)NENWN(E|W)|NESEE(SEWN|)NNNNWSWW(SEESNWWN|)N(N|E))|NE(EEENESS(NNWSWWEENESS|)|NWN(W|N)))|E(EESEWNWW|)NN)|S)|SSSWSWSSENEEN(W|N(ESSEE(ENWN(WSNE|)ENWNNE(NWES|)S|SWWSESSEN(N|ESESENEN(EENNW(NEEEE(SSWW(NEWS|)SESSWNWWSSE(SEEN(ENNEENW(W|NEE(N|ESSSEEEESWWSWSSWSEENNESSESWSESSEENESEENENEESWSEENESSENENWNNWSWNWWNWSWSW(S|NNNNNESS(S|ENESEEEENWNWNEEES(W|SSEEEEESSSENESENNNWSWNNNWWS(WNNNESENNWWWNNNESSENNNNEEENWNNWNENN(WSWNWSS(WNWESE|)SE(SWS(EENSWW|)SW(S(E|WWSESSWWN(E|NNN(WSW(SSSWWWNEN(ESNW|)WWSWNWSWSEESSEES(SENNE(SSSEWNNN|)N(WWWNSEEE|)ESEEEN(WWNNNSSSEE|)ESSSSENNN(SSSWNNSSENNN|)|WWWNWN(W(SSSW(W|SEEE(NWNSES|)SSSSWNW(NENWWEESWS|)SS)|NWWWS(EE|WNNEEEN(WW|NEN(W|E(SSWSNENN|)NN))))|E))|N)|EE)))|N)|N)|ESSSSESENN(W|EEENEE(NWN(EN|WSWS)|SWSESWWNWWSSWWSEEEN(N|ESSSWWSEESWWSSSSSSENENWNNNESES(SSENESE(NNWWNNWNENE(NNNWSSW(NNNEENN(SSWWSSNNEENN|)|S)|SSEEE(SW(S(S|E)|WW)|N))|SS(EE|WS(E|WNWN(EE|WSWWSEEESSE(NEWS|)SSWNWNWN(WW(NNNNNNNWNWNW(SSESESW(ENWNWNSESESW|)|NNNE(EE(EE|SWS(WNSE|)SE(N|S))|NWWSSS))|WWSEESE(ESSWSWSSSESWSWWSEEESWSWSESES(WSWS(E|WSWNNWSSWSSWNNWWWNEEENNNWSWNNWNWSSWNNWNENNWNNNNESENNEENNEESWSEEESWSSEEN(ENE(SSWS(WSWWSEESSSE(NNEWSS|)SESW(S|WWW(SS|NE(NNNWSWS(WNWNEENWNEN(NWWW(NEN(EESWENWW|)W|SE(E|SSWNW(SSE|NWNE)))|EE)|E)|E)))|E)|NNWNN(ESE(E|S)|WNWSW(SSEE(NWES|)S(E|S)|WNWSW(WSSWWWWS(EE|WWWWWWSWWWSWNWWSESWWNWWNWNWNNEENWNNWWSWNWNENENNESESES(ESWSEENNN(WNENNENWWNE(N(NN|WWSSWS(EESW(W|S)|WWWSSWNWNW(WWWNWSWWNNWSWNNWWS(ESWENW|)WNW(NEENN(WSWNWNN(WSSWENNE|)ESENN(ESSNNW|)W|ESEEN(W|NESSSE(N|S(WWNWWEESEE|)S(ENEES(EES(E(ESNW|)NN|WW)|W)|S))))|SWNWSW(SEEWWN|)W)|SSSSW(WWWWW(NEWS|)SSWSW(W|SSES(W|EEEEESENEEESSWNWSWSWNWNWWW(W|SSEE(NWES|)SE(SWSSSESWSESWWWSW(NNNEN(W|E(SSWENN|)NNNN)|SSW(NN|SES(WWNSEE|)EEEESWSEES(WW|ENENNNESSENENNW(S|NNNESEEESWSESWW(NNWESS|)SSEEN(W|ESENNEENESEENWNNWSWWNWNNEENESES(WW(W|S)|EENNW(WNENNWWS(E|WWS(EE|WNNEENEEEENN(NESESSSSWS(SSSSWS(WNSE|)SENENNESESWSESENNESSENNNENNE(NWWSSWSWNNENNNNWNENENWNEN(ESSSSS(E|SSWNNN)|WWSWNWS(SES(ENSW|)SSW(NN|SSEE(NWES|)SWS(S|WWN(N|E)))|W))|SESE(E(EE|N(W|N))|SWW(SEESEESWSWWSEEENE(NN|SEEN(ESSESS(ENNN(ESSE(NN|S(SEE(NWES|)EESSSESESWWS(WNWNE(E|NWNW(NEESNWWS|)S(W|S))|E)|W))|NNW(SS|N(WSNE|)E))|SSWNWSWWSSWWNWNWWNNWWSSE(SWSSSSW(SESESWSSWSS(SE(NEEESENNWWW(NEN(W|NNEE(SSS(WNNSSE|)ESSESS(WNSE|)EENN(W(S|N(E|W))|E)|ENNNWWNN(W(NEWS|)WSESWSSEEN(ESNW|)W|ESEE(SSS|EE))))|W)|S)|WN(WW|NNNE(NWES|)S))|NNNWWSS(ENSW|)WWWNNESENNEEENNWNNE(NNWNEEEE(SSWS(WNNEWSSE|)EESEENEEES(EENWNWWWWW(W|S)|SWW(NEWS|)S(WNWWEESE|)S)|NW(WWWWWWSESSSWWNN(ESNW|)WSSWNNNEENN(E(N|E)|WSWWSWWW(NEEWWS|)SEEESSWSEEESENEEE(SWS(EE|W(WS(WSWNN(WWN(WSWNWNNEN(E(SSWENN|)E|WWSWNN(EE|WSWSWWSSESSSEEESSESSESSENNESE(SSS(ENSW|)WN(WWSSWSS(ESEEE(EE|NWWN(W|EENWWN))|WNW(SWEN|)NENNNE(NWNNWW(NWN(EESNWW|)WWS(E|S|WWWNNW(WNN(WSSNNE|)EEEENWWNEEN(E(N(EEN(E|WW|N)|W)|SSSESSWWN(E|W(SSEWNN|)WW))|WW)|S))|SSE(N|SSW(SEWN|)N))|SS))|N)|NNENWNE(NWWWSESWS(WNNWNNN(ES(S|EEEE)|NWSSWWNNE(S|N(EE|WW|N)))|E)|EESWSEE(WWNENWESWSEE|)))))|EE)|E)|E)|N))|NN(NN|E)))|N(EESEWNWW|)NN))|S))|N))|W))|N)))|WNNENN)|WWS(E|WWWWNWSWSWSSWNWWNNEN(ES(SWEN|)ENENWNWNNNN(ENSW|)WWSES(SSSEWNNN|)WWWWWWWNNW(NNEEESESS(ENNN(E(S(SS|E)|NN(E|N))|W)|WNW(NWES|)S)|WS(ESWENW|)W)|WWWSESSSEESEESENNNE(NEEWWS|)SSS(SS(SSES(WSNE|)E|WWWN(EE|NWSWWWWNNNW(WNENNESES(SSSEENW(ESWWNNSSEENW|)|W)|SSSSESEE(NWES|)SSWWSW(SESWENWN|)WNWWW(SEEWWN|)NEEEN(WW|ES(S|EE)))))|EE))))))|S)))))))|N))))|N))))|EE)|ESEE(NWES|)SWSEE(N|SWWSSES(ENN(W|EEN(EEEEE(N|ES(ENESEE|WWWWS(EEEE|W(WSWNSENE|)N)))|W))|WWWSWNN(W(S|W)|NNEE(SSWNSENN|)NN))))|WW(W|N)))|NNENWNEN(WW(WWWW|SS)|ESE(SS(WNSE|)(S|EE)|N))))))|W))|ENNWNEE(ENNWW(SEWN|)N(NE(SEWN|)NWNN(WSNE|)NEEENWWN(SEESWWEENWWN|)|W)|S))|N))|E)))))|W)))))|E))))))|W)|N)|NN)|S)|WW)))|NN))))|NN))|NENNW(WWWNN(WSSWNWSSE(WNNESEWNWSSE|)|EES(W|E(NNNNENWWSW(SSENSWNN|)NNNESENESEE(SWSEWNEN|)NWNWWWW(EEEESEWNWWWW|)|E)))|S))))))|NNNNNEENE(EEENNNESEESWWSES(WW|EEENENNWSW(SWEN|)NNNESENESEESWWSSENESESWWWWS(WSSSNNNE|)EEEEEEEENENNNWNENNWSWWWSSW(SESENNNESSS(EN|SWW)|NNWNW(S|WWWNNNNENWNENENEEENWNWNNNWSSSS(WNNWWWSEESWSWNWNWWNNENEEES(WWSWENEE|)EENNENNN(WWSS(ENSW|)S(WNNWWN(EE|WWWSESE(N|S(ENESNWSW|)WSWSSSSWNWWSSE(SS(WNW(S|NNNW(WNW(NENWNN(WSNE|)ESESESS(WNSE|)EENWNEE(SS|NN(ESNW|)WSWNNN(EESWENWW|)WSS(WNWWNEE(WWSEESNWWNEE|)|S))|WWWWSWN(SENEEEWWWSWN|))|SS))|ESENNN(WSNE|)ENESESWSESESE(SSWSESWWNWWNNN(E(NWNNSSES|)ES(WSEWNE|)E|WWW(SSESWSSSWNWWSESEES(WWSWNN|EENNW(NEN(NNNWESSS|)(W|EES(EESWENWW|)W)|S))|N))|NNWNEENE(WSWWSEWNEENE|)))|N)))|S)|EESEEN(ESSESSWSWWW(NNWN(N|EEES(SWNSEN|)E)|SESEEEESSSEEEESEEESEEENENENESSSESENESSWSESESWWNWSWNWWSWWNNWSWWSWWNNWNNN(EEESSE(SWW(NNWSNESS|)S|EN(W|EES(EEN(ESESWWWWS(NEEEENSWWWWS|)|N(WSNE|)N)|W)))|WN(WSSSSE(S(SSE(SWSSSESEEEESSENNENNEEESSWSW(NNEWSS|)WSESESSESWSSENEEEENNNWNNESESEENNNWW(SESNWN|)WNENNWSWNNWNEEN(WWWSS(WWNWSWWNEN(WNWSSSWWNN(ESNW|)WSSWSEEEEESWWWW(EEEENWESWWWW|)|EEE(S|N))|SESSS(ENSW|)W(NN|WS(W|EESWWSESSEENWN(SESWWNSEENWN|))))|EESS(SEEEENNNESEESSESSESSESSEESESSWNWWWN(NWSSWNWNNE(S|E(E|NWWWSSSSESSESEES(ENEN(ESSEE(SW(SE|WWN)|ENEENNWWNNEEEENWNWWNWNNNWSSWWW(SSENEESES(EE|W(WNSE|)SSSS(WSEWNE|)EE)|WNEEENWWNWNENNWWNWWNNWWSES(WWNWWSESWSS(ENSW|)WNNNNNENENWWSWW(SESSNNWN|)NNNNWNWW(NNWWWS(WWNWNWNWNNWNWSWWNNWW(N(WSNE|)EEEES(WSNE|)EEN(ESS(W|EEEESWSESS(ENNEEENENWNWN(WSW(SSEENW|WWN(WWSEWNEE|)EE)|EEEEEEESWWWW(SEESWSW(N|WSSSW(NNWSWN|SEEES(W|SEEENWNW(NWWNEEEEENESSWW(SESSESSSW(NNWSWWW(NEEWWS|)S|S(SWEN|)EEENNNNNW(N(WSNE|)ENNW(S|NENENWNNN(ESSESSSEEESWSWSEENEESWSWSESWSWWNNWN(EESSNNWW|)NNN(E|W(N|SSSSSSE(N|SSW(N|SSENESENENEENW(WWWSEWNEEE|)NEESSSENESSSSSEEESWWSSSENNESEESSWNWSSESW(SEEE(SSWNWWSSSWW(NN(ESNW|)WW|SEES(SESS(WNSE|)EE(NNW(NWNEE(NWWN(N|EE)|S)|S)|SSS)|WWWW))|NN(WSNE|)NNNNWNNW(SS|NWNNNNESESS(WNSE|)E(NNNNNNNNWWWWNNNNNNEESSW(N|SESWSEENNNNNE(NWNENWWSSWNNWSSWWNWN(EESNWW|)WSWSSSEEN(WNEWSE|)ESE(N|SWWSSESSWSEE(NNNNWESSSS|)ESSENEE(NWWEES|)SWS(ESNW|)WWW(SESWSSSENN(SSWNNNSSSENN|)|WNENWW(SS|WNW(NEN(E|NNNWW(SEWN|)NNWNWNW(N(WSNE|)EESE(NEWS|)S|SSES(E|W)))|S))))|SSSSS))|S(W|SS))))|WNWWN(NNNW(N(E|WWWS(WNNEENENN(ESSSWENNNW|)WW(NEWS|)WS(SENEWSWN|)WW|EE))|SSS)|EE))))))|WWSSW(WSS(ENEE(SWEN|)NN|SWN(WSWWEENE|)NN)|NN)))|SSSS))|W)|S))))|W))|W(NW(NNWWSES(NWNEESNWWSES|)|S)|S)))|W)|SSE(SWSWS(EENENEEESSWNWSSSWN(WSSEEEENN(WSNE|)E(ESESWW(N|S(W|EEE(SWEN|)EN(W|E)))|N)|N)|WW)|N))|EE)|SES(W|E))|SEESSE(SSE|NE))))|WWN(EE|W(W|S)))|WWS(WNNWSS(S|WNWNNNE(ESWSNENW|)NWWWN(EENE(S|NNNENN(E(NNWSNESS|)SE(S(E|W)|N)|WWS(E|W(NWSWNSENES|)SESSW(N|S))))|WSSSSWN(NNN|WWWSW(N|WSSEESEESE(SWSWNNWWNWWSSS(EEE(NWWNSEES|)SESSW(N|SEENE(S|N(E|N(WSNE|)N)))|WNNNWNNNWSWSSSWNNNNNNWSWNWWSS(WNNNNWSWNW(SSEESNWWNN|)NENESEESES(W|ENEEES(EENWNE(NWWWS(WWWNENN(WSWW(WWW(S|WW)|NEN|SE)|ES(ENSW|)S)|E)|ESSSS(WWW(NEEWWS|)S|SESWSE))|WW))|SESENE(NWWNSEES|)SSWWW(S(WWWNEE|SES(SWNSEN|)EEN(EEEE(NWNNSSES|)SS(ESWENW|)WWN(E|W)|WN(E|W)))|N)))|NE(NN(WWW(NE|SEE|WW)|EE(S(E|W)|NNW(NEWS|)S))|S))))))|E))))|EE)|W(N|W)))|NN)|WWNWSSWNNWSSWNNWSWNNW(WSESWENWNE|)NEEENENWWN(EENNEESWSSE(ESWWSWS(EENESNWSWW|)WW|N)|WSS(WNSE|)E))|NN)|E)))|W))|E))))|S))))|N))|S))|SWSESWWNW(N(NNNNWESSSS|)E|SSSS))|E(EE|N))|NN))|E)|E)|S))|SS)|S))|W))))|W))|W)|N(E|NWS(WNN(W|EE)|S))))|W))|WW(WW|N))|NW(NEWS|)S)|EESSWN)|W))|WWWWNE(EE|NWWN(E(E|N)|WSSS(ENSW|)WNWN(WSWNWWNWSSWNNWSWSWS(WWWWWWWNENWWNNWSWSSE(ESWWWNWNENNWWWWNWNEEENENWWSWNWSWNWWSESESWSWNWN(WNWWWSWWW(SSESESSS(ENNNESSSEEENENWWNN(ESEEEE(NWES|)SESS(WNWNWSS(E|W)|EE(E|NNN(E|W(W|SS))))|NWW(NEWS|)S(ESSSEWNNNW|)WWN(E|W))|WNW(N(N|E)|S))|NNNENESS(WSEWNE|)EENWNNNWWNW(NENESSEEESSENNEEESSWW(NEWS|)SEEENEENNWW(SEWN|)N(WWNWWS(WNWW(SEWN|)NEEEENNN(EEEEENN(NESS|WSW)|WSWS(E|WWWSWW(S|NNNEES(WSNE|)EENWNWWWN(NN|EEEESE(S|N)))))|E)|EENENESEEN(W|EENWN(EESENE(SSWSW(SWSWWWWW(NEEEENE(WSWWWWEEEENE|)|SSSES(ENNWNEESSEESSSSENESESESWW(NWWW(S|WW(NENE(NWNEWSES|)S|WW))|SEESSENNNENENN(EESSW(N|SES(WW(N|SS(WNN|ENE))|E))|NNNWWWSWS(SEEN(W|E(NWES|)SSW(S|W))|WNNNW(N(WSWNSENE|)EE(NW(N|W)|S(EEEEE|S))|SSS))))|WWW(NEWS|)WWWWWNW(SSEES|WNN)))|N)|EE)|N)))|SS(S|EE)))|E)|N)|EE(N|EEEE(NWES|)EEE))|E))))|W(SSEWNN|)N(W|E|N)))|NWNWSSWSE(ENSW|)SSWWWNNNE(SSEWNN|)N(W|E)))))|W)|NN)|NN)|W))|N)|W))|SE(SWSWENEN|)E)|WW))|E)|S(W|S))|NNE(S|E))|WW)|E)|NNEEEENNESSENNNEE(SWEN|)ENENNWWS(E|SWNNWNNWNWWSESESWWNWNNWNEEENNNNWWWW(NEENNENNWWS(W(SSENSWNN|)NNE(NWES|)EEESES(ENSW|)WSSE(S(WWNSEE|)ESWSESWSEENNESE(NNWWNEENE(WSWWSEWNEENE|)|SSW(SW(SSEEE(ESENESEN(SWNWSWENESEN|)|NN(WSWENE|)N(EE|N))|WN(W|E))|N))|N)|E)|SSEEE(NWWEES|)SWWWSSSSSE(SWSSENEES(SSWWWNEEN(SWWSEEWWNEEN|)|ENN(WWN|EESWS))|NN)))))|E)))|NENE(SSWENN|)NW(WSNE|)N)|W)|EEE))|W))|S)|NEEEEEEN(EE(ESWSS(WWWW(S|N(EEENSWWW|)W(S|W))|S)|NW(NEWS|)W)|WWWW))|EEESE(SSSEWNNN|)E))|N(W|N)))|E)|N)|N)|NNNN(WWWSWWSS(SWSWNN(WSSWNNW(SWSSEN|N)|E)|EEN(W|ENESSW))|NENNW(W|S)))|N))|NW(NWWWNEEEE(EEENWWWWNNWSSWNNNEEEEESS(WWNEWSEE|)ENE(NWN(WWWWNWWWWWSWSESENE(SSWWWWN(E|WSSWNWSSW(SSSWW(N(EN|WS)|SEESESWSW(SEEEENENNE(S|EE|NNNWWWW(SEEESWW(SS(SW|EN)|W)|NEEEN(ESENN(E(SSS(W|EEE)|E)|WW)|WW)))|WWNENES(NWSWSEWNENES|)))|NNNWWWN(EEEESENEENWWWNENESEEN(EENESEENNEEENWN(WWW(N|S(WWS(WS|EES)|EE))|EESSEEE(NNWW(SEWN|)NEEEEES(EENWN(E|WWN(W(N|WS(E|WWW(S|N)))|E))|WW)|SWWSWWW(SEEEWWWN|)N(WSNE|)EE))|W)|WS(SEEEWWWN|)W)))|N(W|EE))|E)|SE(SWEN|)NEEE(SWWEEN|)NE(NWES|)S)|S)|S)))))))))|S)|EE)|S)|WWWSSWWSSEE(NW|SWS))|S)|SWWWSWNNE(WSSENEWSWNNE|)))))|E)|NN))|N))|S(WNSE|)S))|WW)|SS))|EE(NWES|)SS)|NN)|S(WWSESNWNEE|)E))|S)|SSE(SWEN|)N)))|E))|S(WSSWENNE|)E)|SWSW(SEE(SESWSESSWSSWWSSWNNNEENN(E|NWWWSS(EENWESWW|)SWSWSS(SENNE(SSS(EEESEESSWWWW(SWWWSES(WWNWESEE|)ESSEEEEEENWWWNEENWN(EEESS(WNSE|)(ENNESENNWNEE(NWWWWW(NWNNWN(ENNE(ENWESW|)S|WSS(ESNW|)WW)|SES(ENSW|)W)|S)|SSS(E|WWSSSWSESSS(ESEEEE(NWWWN(W|EEEN(NESSEWNNWS|)W)|SWSWNW(S|W))|WWSWNNEENWWNENNWNN(WSW(WSS(WWNN(ES|WNW)|SEE(SWEN|)N(WNEWSE|)E)|N)|EES(S|W)))))|WWS(W(SSENSWNN|)W|E))|NE(NWES|)EE)|W)|N)|WNNW(SSWENN|)NNNNWNENWWSW(S(E|SS)|NWNNEEEEE(S(SSESWSEE(SWSWNSENEN|)NNEEN(EESWENWW|)W|WWWW)|NWWWN(WSWENE|)(EEE|N)))))|N)|NN)))|S))|W)|EE)|NNN(E(E|SS)|WWSSEN))|EEE))|NWW(NEEWWS|)(S|W))|EENWNE))|E)|E))|NW(NENSWS|)WSW(S(WW|E)|N))))$";

	public static char[][] themap = new char[height][width];
	public static char UNKNOWN = '?';
	public static char ROOM = '.';
	public static char WALL = '#';
	public static char HDOOR = '|';
	public static char VDOOR = '-';
	public static int currx, curry;
	static String outfname = "files/rooms.txt";
	static BufferedWriter bw;

	public static ArrayList<Coord> parseIt(String s, Coord curr) {
		ArrayList<Coord> ret = new ArrayList<Coord>();
		if (s == null || s.length() == 0) return ret;

		String next = null;
		Coord temp = new Coord(curr.x,curr.y);
		char c = s.charAt(0);
		switch(c) {
		case 'N':case 'S':case 'E':case 'W':



			//check for top-level pipe (NEW)
			int pos2 = 0;
			int paren_count = 0;
			boolean found_toplevel_pipe = false;
			while (true) {
				if (s.charAt(pos2) == ')')
					paren_count--;
				else if (s.charAt(pos2) == '(')
					paren_count++;

				if (paren_count == 0 && s.charAt(pos2) == '|') {
					found_toplevel_pipe = true;
					break;
				}
				pos2++;
				if (pos2 >= s.length())
					break;
			}
			if (found_toplevel_pipe) {
				ArrayList<Coord> al3 = new ArrayList<Coord>();
				al3.addAll(parseIt(s.substring(0,pos2),curr));
				al3.addAll(parseIt(s.substring(pos2+1),curr));
				return al3;
			}




			String[] parts = s.split("\\(|\\)|\\|");
			//System.out.println(temp.x+","+temp.y+ "  " + parts[0]); //TEST
			for (int i=0; i < parts[0].length(); i++) {
				char c2 = s.charAt(i);
				temp = move(c2,temp.x,temp.y);
			}
			//printRoom();
			next = s.substring(parts[0].length());
			if (next.length() == 0) {
				ret.add(temp);
				return ret;
			} else {
				if (next.charAt(0) == '|') {
					ret.add(temp);
					ret.addAll(parseIt(next,curr));
					return ret;
				} else
					return parseIt(next,temp);
			}
		case '|':
			next = s.substring(1);
			return parseIt(next,curr);			
		case '(':
			//find the group, parse it, parse the rest (NEED WORK BELOW)
			int pos=0;
			int num_skips = 1;
			while (s.charAt(pos) != ')' || num_skips > 0) {
				pos++;
				if (s.charAt(pos) == '(')
					num_skips++;
				else if (s.charAt(pos) == ')')
					num_skips--;
			}
			String group = s.substring(1,pos);
			String rest = s.substring(pos+1);
			ArrayList<Coord> al = new ArrayList<Coord>();
			if (group.endsWith("|")) {
				//empty group case
				al.add(new Coord(curr.x,curr.y));
				group = group.substring(0,group.length()-1);
			}
			if (rest != null && rest.length() > 0) {
				char next_char = rest.charAt(0);
				al.addAll(parseIt(group,curr));
				if (next_char == '|') {
					al.addAll(parseIt(rest,curr));
					return al;
				}
				ArrayList<Coord> al2 =  new ArrayList<Coord>();
				for (Coord c3 : al) {
					al2.addAll( parseIt(rest,c3) );
				}
				return al2;
			} else {
				return parseIt(group,curr);
			}
		case ')':
			//NEEDED?
			break;
		default:
			break;
		}
		//printRoom();


		return ret;
	}



	public static void main(String[] args) {

		smap = smap.substring(1,smap.length()-1);
		for (int row=0; row < themap.length; row++) {
			for (int col=0; col < themap[row].length; col++) {
				themap[row][col] = '?';
			}
		}
		themap[starty][startx] = ROOM;

		//TESTING
		/*
		smap = "NNNNN"; 
		smap = "NNNNN|EE"; 
		smap = "NNNNN(EE)"; 
		smap = "NNEE(NN|SS)"; 
		smap = "NNEE(NN|SS)E";
		smap = "NNEE(NN|SS)(E|W)"; 
		smap = "NNEE(NN|SS(EE))"; 
		smap = "NNEE(NN|SS|)E"; 
		smap = "NNEE(E|N(E(WN|)S|E(N|E)))";
		 */
		//smap = "N(E(S|)N|W(S|E))"; //not working
		//smap = "E(S|)N|W(S|E)"; //not working
		//smap = "E(S|N)N|W(S|W)"; //not working (CASE: need to break this on '|' in two parts!!

		//printRoom();
		parseIt(smap,new Coord(startx,starty));

		//printRoom();
		findFurthest();
		writeRoomsToFile();
	}

	public static Coord move(char c,int currx, int curry) {
		switch(c) {
		case 'N':
			curry--;
			themap[curry][currx] = VDOOR;
			themap[curry][currx-1] = WALL;
			themap[curry][currx+1] = WALL;
			curry--;
			themap[curry][currx] = ROOM;
			themap[curry-1][currx-1] = WALL;
			themap[curry-1][currx+1] = WALL;				
			break;
		case 'S':
			curry++;
			themap[curry][currx] = VDOOR;
			themap[curry][currx-1] = WALL;
			themap[curry][currx+1] = WALL;
			curry++;
			themap[curry][currx] = ROOM;
			themap[curry+1][currx-1] = WALL;
			themap[curry+1][currx+1] = WALL;	
			break;
		case 'E':
			currx++;
			themap[curry][currx] = HDOOR;
			themap[curry-1][currx] = WALL;
			themap[curry+1][currx] = WALL;
			currx++;
			themap[curry][currx] = ROOM;
			themap[curry-1][currx+1] = WALL;
			themap[curry+1][currx+1] = WALL;
			break;
		case 'W':
			currx--;
			themap[curry][currx] = HDOOR;
			themap[curry-1][currx] = WALL;
			themap[curry+1][currx] = WALL;
			currx--;
			themap[curry][currx] = ROOM;
			themap[curry-1][currx-1] = WALL;
			themap[curry+1][currx-1] = WALL;	
			break;
		default:
			System.out.println("SHOULD NOT HAPPEN: " + c);
			break;
		}
		return new Coord(currx,curry);
	}


	public static void printRoom() {
		String s = "";
		for (int row=0; row < themap.length; row++) {
			for (int col=0; col < themap[row].length; col++) {
				if (themap[row][col] == UNKNOWN)
					themap[row][col] = WALL;
				if (row==starty && col==startx) {
					s += 'X';
				} else
					s += themap[row][col];
			}
			s+="\n";
		}
		System.out.println(s);
	}

	public static void findFurthest() {
		System.out.println("Building graph...");
		//create the graph
		HashMap<String,Vertex> vertices = new HashMap<String,Vertex>();
		String sid;
		for (int row=0; row < themap.length; row++) {
			for (int col=0; col < themap[row].length; col++) {
				sid = col + "|" + row;
				if (themap[row][col] == ROOM) {
					if (!vertices.containsKey(sid)) {
						vertices.put(sid, new Vertex(sid));
					}
				}
			}
		}

		//for each node, add its edges
		HashMap<String,Edge1> edges = new HashMap<String,Edge1>();
		int maxrow = Integer.MIN_VALUE;
		int maxcol = Integer.MIN_VALUE;
		String toid = "";
		for (int row=0; row < themap.length; row++) {
			for (int col=0; col < themap[row].length; col++) {
				if (themap[row][col] != ROOM) continue;
				sid = col + "|" + row;

				if (row > maxrow) maxrow = row;
				if (col > maxcol) maxcol = col;

				Vertex v = vertices.get(sid);
				Vertex v2;
				String edgeid = "";
				Edge1 edge;
				//up node?
				if (themap[row-1][col] == VDOOR) {
					toid = col + "|" + (row-2);
					v2 = vertices.get(toid);
					edgeid = v.name + "|" + v2.name;
					if (!edges.containsKey(edgeid)) {
						edge = new Edge1(v2, 1);
						edges.put(edgeid, edge);
						v.adjacencies.add(edge);
					}
				}

				//down node?
				if (themap[row+1][col] == VDOOR) {
					toid = col + "|" + (row+2);
					v2 = vertices.get(toid);
					edgeid = v.name + "|" + v2.name;
					if (!edges.containsKey(edgeid)) {
						edge = new Edge1(v2, 1);
						edges.put(edgeid, edge);
						v.adjacencies.add(edge);
					}
				}

				//right node?
				if (themap[row][col+1] == HDOOR) {
					toid = (col+2) + "|" + row;
					v2 = vertices.get(toid);
					edgeid = v.name + "|" + v2.name;
					if (!edges.containsKey(edgeid)) {
						edge = new Edge1(v2, 1);
						edges.put(edgeid, edge);
						v.adjacencies.add(edge);
					}
				}

				//left node?
				if (themap[row][col-1] == HDOOR) {
					toid = (col-2) + "|" + row;
					v2 = vertices.get(toid);
					edgeid = v.name + "|" + v2.name;
					if (!edges.containsKey(edgeid)) {
						edge = new Edge1(v2, 1);
						edges.put(edgeid, edge);
						v.adjacencies.add(edge);
					}
				}

			}
		}

		System.out.println("Calculating shortest path through most doors...");
		sid = startx +"|" + starty;
		Vertex vstart = vertices.get(sid); //start vertex
		Dijkstra.computePaths(vstart); // run Dijkstra

		int largest_path = Integer.MIN_VALUE;
		Vertex largest_room = null;
		for (Map.Entry<String, Vertex> entry : vertices.entrySet()) {
			Vertex v = entry.getValue();
			List<Vertex> path = Dijkstra.getShortestPathTo(v); //no path is list of size 1 (itself)
			//System.out.println("Path from,to  " + vstart.name + "," + v.name +"  " + path + "   path.size(): " + path.size());
			if (path.size() > largest_path) {
				largest_path = path.size();
				largest_room = v;
			}
			//System.out.println("path.size(): " + path.size());
		}
		System.out.println("maxrow: " + maxrow + "   maxcol: " + maxcol);
		System.out.println("\nLargest number of doors required to pass through to reach a room?: " + (largest_path-1) + " doors  to reach " + " to reach " + largest_room.name);
	}

	public static void writeRoomsToFile() {
		File fout = new File(outfname);
		FileOutputStream fos;

		try {
			fos = new FileOutputStream(fout);
			bw = new BufferedWriter(new OutputStreamWriter(fos));
			for (int row=0; row < themap.length; row++) {
				for (int col=0; col < themap[row].length; col++) {
					if (themap[row][col] == UNKNOWN)
						themap[row][col] = WALL;
					if (row==starty && col==startx) {
						bw.write('X');
					} else
						bw.write(themap[row][col]);
				}
				bw.newLine();
			}			
			bw.close();
		} catch (FileNotFoundException e1) {
			e1.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

}

