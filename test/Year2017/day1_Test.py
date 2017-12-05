from unittest import TestCase


class Day1:
    def calc(self, captcha):
        sum = 0
        for i, n in enumerate(captcha):
            if n == captcha[(i + 1) % len(captcha)]:
                sum += int(n)
        return sum

    def captcha(self, captcha):
        l = int(len(captcha) / 2)
        sum = 0
        for i in range(l):
            if captcha[i] == captcha[(i + l)]:
                sum += int(captcha[i]) * 2
        return sum


class Day1Test(TestCase):
    def setUp(self):
        self.day = Day1()

    def test_case1(self):
        sum = self.day.calc('1122')
        self.assertEqual(sum, 3)

    def test_case2(self):
        sum = self.day.calc('1111')
        self.assertEqual(sum, 4)

    def test_case3(self):
        sum = self.day.calc('1234')
        self.assertEqual(sum, 0)

    def test_case4(self):
        sum = self.day.calc('91212129')
        self.assertEqual(sum, 9)

    def test_puzzle(self):
        sum = self.day.calc(self.puzzle())
        self.assertEqual(sum, 1029)

    def puzzle(self):
        return '6592822488931338589815525425236818285229555616392928433262436847386544514648645288129834834862363847542262953164877694234514375164927616649264122487182321437459646851966649732474925353281699895326824852555747127547527163197544539468632369858413232684269835288817735678173986264554586412678364433327621627496939956645283712453265255261565511586373551439198276373843771249563722914847255524452675842558622845416218195374459386785618255129831539984559644185369543662821311686162137672168266152494656448824719791398797359326412235723234585539515385352426579831251943911197862994974133738196775618715739412713224837531544346114877971977411275354168752719858889347588136787894798476123335894514342411742111135337286449968879251481449757294167363867119927811513529711239534914119292833111624483472466781475951494348516125474142532923858941279569675445694654355314925386833175795464912974865287564866767924677333599828829875283753669783176288899797691713766199641716546284841387455733132519649365113182432238477673375234793394595435816924453585513973119548841577126141962776649294322189695375451743747581241922657947182232454611837512564776273929815169367899818698892234618847815155578736875295629917247977658723868641411493551796998791839776335793682643551875947346347344695869874564432566956882395424267187552799458352121248147371938943799995158617871393289534789214852747976587432857675156884837634687257363975437535621197887877326295229195663235129213398178282549432599455965759999159247295857366485345759516622427833518837458236123723353817444545271644684925297477149298484753858863551357266259935298184325926848958828192317538375317946457985874965434486829387647425222952585293626473351211161684297351932771462665621764392833122236577353669215833721772482863775629244619639234636853267934895783891823877845198326665728659328729472456175285229681244974389248235457688922179237895954959228638193933854787917647154837695422429184757725387589969781672596568421191236374563718951738499591454571728641951699981615249635314789251239677393251756396'

    def test_case_1p2(self):
        sum = self.day.captcha('1212')
        self.assertEqual(sum, 6)
        sum = self.day.captcha('1221')
        self.assertEqual(sum, 0)
        sum = self.day.captcha('123425')
        self.assertEqual(sum, 4)
        sum = self.day.captcha('123123')
        self.assertEqual(sum, 12)
        sum = self.day.captcha('12131415')
        self.assertEqual(sum, 4)

    def test_puzzle2(self):
        sum = self.day.captcha(self.puzzle())
        self.assertEqual(sum, 1220)