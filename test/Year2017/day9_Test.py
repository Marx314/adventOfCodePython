from unittest import TestCase


def group_score(stream):
    i = 0
    nesting = 0
    score = 0
    garbage = False
    garbage_collector = ""
    while i < len(stream):
        letter = stream[i]
        if letter == '!':
            i += 1
        elif garbage and letter != '>':
            garbage_collector = garbage_collector + letter
        elif letter == '<':
            garbage = True
        elif garbage and letter == '>':
            garbage = False
        elif letter == '{' and garbage == False:
            nesting += 1
        elif letter == '}' and garbage == False:
            score += 1 * nesting
            nesting -= 1

        i += 1
    return score, len(garbage_collector)


class Day9Test(TestCase):
    def test_simple_part1(self):
        score, _ = group_score('{}')
        self.assertEqual(score, 1)
        score, _ = group_score('{{{}}}')
        self.assertEqual(score, 6)
        score, _ = group_score('{{},{}}')
        self.assertEqual(score, 5)
        score, _ = group_score('{{{},{},{{}}}}')
        self.assertEqual(score, 16)
        score, _ = group_score('{<a>,<a>,<a>,<a>}')
        self.assertEqual(score, 1)
        score, _ = group_score('{{<ab>},{<ab>},{<ab>},{<ab>}}')
        self.assertEqual(score, 9)
        score, _ = group_score('{{<!!>},{<!!>},{<!!>},{<!!>}}')
        self.assertEqual(score, 9)
        score, _ = group_score('{{<a!>},{<a!>},{<a!>},{<ab>}}')
        self.assertEqual(score, 3)
        score, _ = group_score('{{<a!>},{<a!>},{<a!>},{<ab>}}')
        self.assertEqual(score, 3)

    def test_part2(self):
        _, garbage_length = group_score('{<>}')
        self.assertEqual(garbage_length, 0)
        _, garbage_length = group_score('{<random characters>}')
        self.assertEqual(garbage_length, 17)
        _, garbage_length = group_score('{<<<<>}')
        self.assertEqual(garbage_length, 3)
        _, garbage_length = group_score('{<{!>}>}')
        self.assertEqual(garbage_length, 2)
        _, garbage_length = group_score('{<!!>}')
        self.assertEqual(garbage_length, 0)
        _, garbage_length = group_score('{<!!!>>}')
        self.assertEqual(garbage_length, 0)
        _, garbage_length = group_score('{<{o"i!a,<{i<a>}')
        self.assertEqual(garbage_length, 10)

    def test_puzzle(self):
        score, garbage_length = group_score(self.puzzle())
        self.assertEqual(score, 15922)
        self.assertEqual(garbage_length, 7314)

    def puzzle(self):
        return """{{{{{{{<!!"!!!>},<>},{<o!>},<u!!i!!'!>,<!!!>,e{'e!!!>},<!i>}},{{<"o!!"!>,<>},<!io<>},{{},<!!!>!>,<o"e!<!!!>{,!!!>{a!o,au!>},<>}}},{{{<e!}>},{{<!>,,e!!!>!!,>},{<a!!!>'!!!>!!!!,!!!>!!!>!>},<<{"!!>}},{{<!>>,<!>},<i!>!<>},{<!!<u,a"!>},<o{{!!{!!!>i,!>,<i{!u>,{<a!>e}o!>!>e>}}}},{{<i<!>,<!!!>,<ei,!>a>,{}},{<!!!>},<e'>,{}},{{<!!!!u<,'}!>,<"o<>}}}},{{{{{{<!>,<o!!!auii!!!!!>!!!>,<{>}},<},!!!>!!!!!>>},{<'u<"{>,{<!!!!e!>,<'a!!i<!>,>}},{}},{{<i}<!u<{!!!}!!e!{!,>}},{<!!e,!>i>,{}}},{{<i!!!>},<{''i!!!>,!e!>},<!>"a{>,<!!'u!!!>},<>}},{{{},<i!>},<<!>},<">},{{<!>,<o!!!!e{uee!!}o<ei{i!>,<!!!>,<>},<,!>},<a!>>},{{},{<}i,!'!!<!!!>}>}}}},{{{{{},{},{{<i!>,<!"!!!>!!!>''>,{}},{{<!>},<u!a!!!>!u!"'!!{!!!>!!!>!!i!!!>,<,a!!!>i!>},<">,{}},{<!!!eoo!!!!ai'!!u!!!>!o>,{<,!!!>aai}{}}"'>}},{{},<i'ia,!!!>o!>,<"!!u!>>}},{<!!!>{u!!!>,<,<!>},<'<}<'"!>},<!u>}}},{{{{<}!!a}!>},<'>},{}},{{{{{},{{<i{!'u}}{>,{{{{<}!>,<!!!!uau!{''!!}ua>}}},{}}},{{{<!!},!!""!!!>,<i!'!{!>},<o>},{<a!u!!"<!>},<"!,{<<e!!<!!u!>},<!o!!{}>}}}}},<,o}!>,<!!!!'!'a!!{>}},{{{<<>},{{<ui{!!i!>{'!!!>},<'>}}},{<{!!!>},<!a!e!!!>o'i!!<'!>,<o!!e!!"!>,<!>>},{<{a>}}}},{{{{<"{!!!>,e!!!>"a!!}!!!,!>>},<o!!!>>},{{<o!{}!!!>},<!!,!!",!>!!!>!>,<ee!>,<!>!u>,<!oo"u}!!ua!>},<!>},<iie>}},{{<!!!>>},<!!e{!!!!!!!>},<}!!{}!!}<,>}}},{}},{{{<!>!>},<e",!>,<!>,<!>{!!<!>oi>},{<!>!!!>{}o!!!>!>}a!!>}}}},{{{{},{<"!!u">}},{{{<"e!>,<u{<}>},{}},{<!!!>,!!!>!>,<,!}!!!!'ei!!i,>,{<!!a"ua!!!>>}}},{}},{{<!!a!!!>!!}eu!!}{{a"">}},{{<u!>,<!>},<!!!>oi!!!>!>!>},<'e{u!'}!>,<!>},<!e>,{<u!!!>}!u<!a>}},{{{<!><!>},<!!!>ii,>}}},{<!>u{'!!!>{i!o}}e!!!>},<a!!!>,<>}},{}}},{{{{{{<ao!!>},{}}},{{<"!!<!>},<>},{<>}}},{<{>},{{<!!!>e!>},<u!!,!!ou}i'e"i>},{{{{}}},{<o!!'!o!!!!!>!ao{<!>>}}}}},{{{{<}}!!!>o!><}o!!{!!!>i!!,>},{{<!!!>'!!!><!>,<>}}},{{{{<o!>!>},<,!!!>o{i{>},{{{{<!>},<a!uo",!>,<!>},<e!>{,}!>},<!>,<>}},{}},{}}}},{{<a!>},<"i!!!!!>,<!!!>"!!oa!!!>!!{!!!!!>!a>,<<{!!!>,<!>"}!>},<!>,<!"!!!"!!ou!>{u!!!>>},{{<<!>,<!!'!!'o"!!!!o"}!i>}},{<}!!}!!}<{>,<!!!>,u!>},<o!ae'u!>},<!>},<<u!e>}}},{{{{<!>eui",o!!!>!>"i>,{<!!!,!!u!!>}},{{<!<>}},{<'!>,<ia!!!!!>},<ea!!!o!>!!!>!<'!e!>},<>,<>}},{{{{<a!!!>!!!>,<'o>}}}}},{{{<!!!>},<,a'a'!!!>,iu"'!>,<}>,{}},{{<!>!>,<<!!!!!>>,<!!!>!>>},{{<,!>,<oe!"!>!!u!',ia'"!>,<!>,<,>},<<!!!!'!!!}}!!!e!!!>,!>},<}!!!!!>,<>},{<"ia!!a!!!!}i!>'>,<"aio!>,<"e"e{!!i!!!>o!{!>!!!!"">}},{{{{{<",u!!{!!{!!<!>},<!u!!,!!!!!>!!!!!!!><"!>},<>},{{<'!"o,!>},<!>,<",!!!!uu!!i!!!>!!"!!!>,<>}}},{{<'!!!!a<<!!!!{u!!,!>},<!>},<o!>},<ouu!!!!!"!!!>>,<!!!>}'{!!a!!"!>},<,ao!!!!!!!>!>!!,<!!!>}>},{},{{{<'!!{"}iu!!e!>!>uo!!}!>,<,!>a>},<<!!!>,!ae!>!>,<a<!!,>}}}},{{{<u!<>},{}},{{{{{{}},<!!!>a!>},<{>}},{<!!<<!>!!!>i!!!>!>},<}{,!!a>,<!>!>"<,e!ee!>,<}!>}"!!!>!!!>o>},{{{},{{},{{{},{<<<'!!!>!>u'i,{!!!>!<!!!>a!>,<>}},<!>!!!><!!!!i!!!>}!,"!!!>!!!>>}}}}},{}}},{{<<eo!!!>!!!!!!!>{{!!!>iou,a'!>,<,>},{}}},{{{}}},{<{!!!>!>,<!!!>},<!!!!}!!!!,a!""}ie!"a>}}},{<!!!!!>!!'',eu!e!>!!!>!>},<>,{{<e''u!>!>,<a!ui}u!>,<>}}},{{<'>}}},{},{{},{{}},{}}},{}},{{{{{<!!""!!,a<>}},{<',<!!!><!!!!},"}>}},{{{{<>}}}}}}},{{{<}>,<<u{!>},<!!"i!aeu!>o"o}o>}}},{{{{{<u!!ee,e>},{<u!!!>!>,<!>},<o>}},{},{<!>o{!!!!i{!>},<o!>"!!u}<e"}!!i">,<i!!!"e!>,<!>,<>}},{{{{<u!>},<!!!>'!!!>!!!!!>}{!>}a!>,<u'!>{!!!>'>,<o"!>,<u>},{<!!uoa>,{{<!!!>,<u}>}}}},{{{{<!>},<!!!><u<>}}}}},{{<!!!<<!!!!,{!!!>!>!!a>},{{<>}}},{<'"a{a}{!'e!!"u'u"!"o!!!>,<i">,<!!!>!!!!<u}!>,<}<!!u>}},{{}}},{{{{{<!!!!a!!u<!>},<,e!!!>iu,>,<'a,uu!!'}!!!>},<},a<!!!>e>},<>},{<{'>,{{}}},{<a!>},<!>,<!!,,u!>},<!><,a>,{}}}},{{{{<eu!!!>},<>}}},{{<!!''!>},<}o!!{>},{},{<>}},{{{{}}},{<}!}u!,,!!!!u!!i}!!!><'!!>,<eo>}},{{{{}}},{{{<!'!!"!>},<{!!!>!i!{e!!>}},{{}}},{<!>ua<<!},!"!>,<!!<!!!>'e<a>,<!!!>!,!u!>,<}"<e!!'!!!>},<!!u!<a>}}},{{{{<{!>,<"!!io!}ei,!!!>o,!>!!}!>,<<'!>,<!!!{>},{}},{{{<!>},<!!"!!!,i!!oe!!}{!>o"!>!!!!,a'!>,<>},{{<i!!i!>},<}!!!!!>a}!!!!'}!!"a>,<!!!>,<e!!!!!>!>,<>}}},{{{},{<}!!eu"eii>}},{{<!!!>},<>}},{{{<{'!>},<!!!>{>}}}},{<"o!!!>i,!>},<oo}!!}<!>},<<>,<a!!!!!<>}},{{<,,!>},<e<!>!!!!}i>},<i'!>,<>}},{},{{<,<"!!!!!!!!!>!'u{>,<{>},{{<>},<{o!>,!!{!!<ooi!!!>,<!>,<!!!}"e!>,<!!">}}},{{{{{<au>,{<!>!>,<"e!},>,{<eo},'!!>}}}},{<e!!>,{<"!'a{!>{i,!!!>,'!!!>!!!i!i!!!!o!>},<i!!!>>}},{<{!!,!>!>},<"!>,<uau!!,i!>},<o!>,<">,{{<',i,!!!>{}oi>},{<ee,!!!>!!!>ai!!!>!>!!'>}}}}},{{{<'!>,<i{!>},<!!i>},{{<a!o!>,<!!!>"!""'!!"!>},<e,e'!>},<!!>}},{{<<>},{<u,!>!!>}}},{{},<'"!>a>}},{{<eo!<'!!'>},{{{<i}<<"!!!>},<e'!>!!i!!"e<!!o<u>},{<!>,<o!e"!!!>io!!,,!!!!!>{!ooo<,a>}},{},{{<!!!>o!!"e'!!i<!!!><!!<o>}}}},{{{<<e!!!>"i!!u<'!!a!"!!!a"io,!>},<>}},{}}},{{{{{<!!,oe>},{{<u!!!!!>}}!>},<!>},<!>!!!>,<!!>}},{{}}},{{{{<'>},{<uoi<u!!e{>}},{<e!!!!ao}!!!>,<'}o!!""!!!>>}},{<uieoai"a>}},{{},{{<,!}>},{<!>},<u'!{!>},<{"a,{{}auo!!{">}},{{{},{}},{<!!!>,'!>{!!!>!!!!u{!,!>!!!>!!i!!o!a,>,{{},{<!>,<!>,<!>,<"a"<,o>}}}}},{{{},{<!e!!!><!!}>}},{{<!>},<o>}}}},{{{<!>,<{i!!'!!!>ii,}>,{<ee!!!>},<o>}},{<!!!!!!!!!>!!{'ao>}},{{{{<!>},<!>"",!!!>,'!!!>}oe}},}!>,<>}}},{<!!ie'!!'{i!!i<}'o!!}<>}},{{{<<aeo!!,a!!ui>}},{},{{<'!!<{!o!"!!!>},<!!u!!!>>}}}},{{{<!!!>!!!>},<!!!>},<!>},<!>i!">,{{<!!'<!>},<"u!!!>!!!!!>'>}}},{{{<!>,<}!!!!'!!!!e!>!>},<!!a!uo<aa!!ao,o>,<!!!!e!!!>iu'!!aa!!>},{<'o!!!>{!!!!!>!!}!i!!!>!!!>!!!>!}a}!!"!i!!!>!!!>>,<"'<{!>,<!>,<!!<}!!!>!<i!!"!"!>,<!>},<<}a>}}},{{<e<>}}},{{{{}},{{<,!>,<}!>},<!!!!a{a>},{<i,a!!!!!>i!!ao!!!>>,<!!!>>}},{{{<>,<eu"<',!>}!!{!!oa!!!>!u"'!!!>,<!>,<>},<,ee'}'!!uo!!!>,<}!!'<u{>},{<!!!>!!!>e!!!>},<!>},<"!>},<!<aa!!!{}"!>!!,a!>,<!>},<>},{{},{<!o>}}}},{{<!!!>}!>!>,<!>},<<!>,<!>{}<!a!'!!i!aa"{>,{<!!i!!!>!!ia!>'!oa>}},{{<o!>,<"!!!e!!<<!>,<!>o!!i>,<!e!>!>,<o<!!!>o!>},<!!!>u!!!>!!>},{},{{{<"!>,<oao!>,!!!!u!e!!!{}u!!,!!}!!!>>}},{<!!,ei!!!>!}!>}!!ua!>!!!!!>!!!>"!'!!!">,<,!!!>,<e!ai!'!>,<,{>}}},{{<a,!!!>,<a!!!>'i!>!!!<!>},<,}!!!!!!o">,{<!!!>,'e'!!!!!a!!i!u!>},<<'!!!>}e,>}}}},{{{{<{e!a!>},<ui,!!!!{>,<uia!i}aoa<<>}}}}},{},{{{{{<<!!'!!,>},{{<<}"u!!!!!>o",!>},<!>},<a>},{}}},{{{<!,'!!<!!!>u!>,<!!!>{!>},<>}},{}}},{{{{}},<!<>},{{{<i!{!>,<!>!>},<}a!>,<a>,{<<!>},<!>},<!!'!>!>!!!>>}},{<>},{<!!!<"!!<!!!>!!!>,<!>},<<!>},<'>}},{<!{<!>,<a!!ae,!!!>'a!!!>'"!!!ue!!>,<a<u!>},<{{!!!>o!!!>i{!,>},{{<,!!!>},<'i!>,<u">},<'!>!>},<{!!{!!!>!>},<o!!ui!>},<!!}>}}}},{{<,"<e{>},{<!>,<!u!>},<>,<u<!!}o>}},{{{}}},{{{{<a!>},<!!!!!>aeoo"!>,<>},<e,!a!!i"ee}!>!>,<>},{},{}}}}}},{{{{{{{<u!>!!',!!!>},<i!>aia!!!!'!>,<">,<!!!>!>,<!!!>!!ie!>o,<>},{<'!!e"!!!"!,">,{{{<<!!uu>}},<o<i!!!>,>}}},{<!>ueo">,<i!>},<o<>}}},{{{<!!!!!!!>!!!!!>,!!!>u'!iaa<uu}>}},{<!!'o{!>!>!<'!>},<!>},<!!!>!{o'!!!>>},{<e!u!>,<!!!>!"!!e}!>},<,i<aea>,{<"!!!>!!!>!>},<}>}}},{{{{{{}}},<,!!u!>i}u!>,<!!!><!>,<i{>},{{<!>!ai!u>,<!>,!>},<<!!!>i!>},<"!!u!uu!!{>},{},{<}!!,!!!>i{o"a!!'ioi>,{}}}}},{{{},{<i,{!!!!"!{o!>,<ou!!!!'"!!o>}},{{{<i,!>!!!>,!>,<a!>},<!!a!!!!!>,<<{!!!!>},{<!'!>>}}},{<>}}}},{{{}},{{<,>,{{<!"a!>,!>,<'a"!>>},{}}},{{{{<,,e}}i<!!!>{ia'o!>},<a<>,{}}}}}},{{{<"!!!>"">},{{<!>},<<"a!>,<<{!>},<!!,e,!!!{>}}},{<a",a!!!i!>},<>,{{<oe!!!>!<eo'e!'!!i,i{!!!!!!!>,<!>,<!!{>}}},{{<!o,!!oi!>,<!!'"{!"!!u>},<'{!!!>!>,<,u}!>!>},<!!>}}},{{{{<!>,<!>!!!>!!!>o!!ae!!!!!!!!!>{!>},<!!!>a'au,>},{{{<,!!!>,<!>},<'>}},{}},{<eea!><,>,{<!!!!!>!{!u!>,<u'{!!}!!!!!>u>}}}},{{{{{{{{<!>}"e!>},<!!'u}>,{<u!o!a<e!!"o!!!!!!"!!}a>}}}},{},{<u}u"!!!!<i!!i}>}},{{<'{!!'!!!>!ii!!o!!!>a!>},<!iu<{a>},<>}},{{<!!<!!!>a}e!>,<!!!!e,,e!<>},<',e!u!!u>}},{<>,<e,!>,<!!uui!>,<>}},{{{},{<a!'!!',,"o,>}},{<o,!!a>},{<!>},<{!!!!ai!>,<!>,<u!!i!>,<!!<!!!>i}!>e>}},{{<>,{<,'!uu!!!>,!o!!!>u{!!!!!ea,e,>}}},{{{{}},{{<{!>,o!>!>},<,<,!!!><"}''oa!!!>!>>},{{<{!!uou!!<i>}}}},{{<!!!>,<!'a!!<>},{<!i!!!!!>>}},{{<<"}!>},<"{o!>},<'!>ie!!a!!a"o!>},<!!!>>,{{{<!!i!>,{!!!!!>!!e!!!!i!>,<>}}}},{<aa!!,u,e>,{<!>!>,<<!!!>!<u,>}},{{},{<}io{!,!!>}}}}},{{{{<""'!!!>!!!'{'u!i<>},{<a,e!!o!!!!">}},{{{<u}a!>},<!>,<!!a!e,<!!ei!>,<,a!!!>,<">}}}},{{{}},{{{<,<ei!!!>u',"!!o'!!!>>}},<!>},<"e,<!!!>!}!o!>},<!!iuo{!>,<u!>},<>}}}}}}},{{{},{{},<!>},<ia!!!>,'!u>}},{{<au'i!!u!!!o!!>,{}},{{<!>!>,<!!e!>e{!!}!!!>"i!!!<>},<>},{{<!>{,!!,{!!!>"!!!ea!{u!>o<o>}}}},{{{{{}},<!!!!!!!e!>,<!>,<{<>},{{<o{a{{u!!">}}},{{},{{<!!!>,<{!!uu!!!>{>,{}},<!!<e!i!!!{!!!>!!"<,<!>,<!>},<>}},{{{{<!!!!!>'oo!!!>,o>,{<!!!!!>!>,<,!>},<'!>,<ioa>,{{<!!<>},<'i!>a'i!>,<}!!'!>!!">}}},{{{{}},{<!!!>>}},{},{{<"u!!u!"!>,<u>},<u!!!>!>e<<u<!>},<a<!i",o!{!>,<,>}},{{<!>,<!!!>}!!!>{oiaou!!}eu!!i">},{{{},<!>},<>},<"a'}a!>{ao!!!>!!!>!>!>,<!!!>i!!'eo>}}},{{<!!io>}},{<!}e!">}}},{{{<!a!!i!!e!!!!!>o!>},<!,aa,i"o!>,<e,>},<a!!{<!!!>!!u!>},<!o{!!!>!>,<!>,<{e>},{{<>},<o!oo>},{{{<,!>,,,o'!o>,{}},{{},{}},{{<!iueieo!!!>!>,<}!>},<'!>},<{!>,<ii>}}},{{{}}},{{<o<!>},<!!,i!>!><!,e!>uo"e}'<>},{{<,!!'!!!>!!eo!>},<o!>,<!!'oe!!!'ea>}}}}}}}},{{{{}},{{{{{<oeo,!>},<!!}{!o<!>},<!>!>,<oo!>!!!!>}},{{},{{<>,{<!!!>a{,'"!!a>}},{<}!u""<}ei!!<'e{>,{<i<i!>,<u>}},{{<,!!a,!!!{,}',u"a!!!>{<iaa>},{{<!!{a'!!!a!>},<u!>,<!>},<!!iiii!!!>,<"!>,<}!>,<ae>},<}"!>!!!>{!!i!'aa!!''>}}}}},{{<}!>,<',aa<!!!!<!!>,{<'!!!>'a!!!>!>,<e<!!a,,<"!!>}},{{<"!!!!!>,!>},<!>>},<{{!>},<!>,<{!!ee!i>},{}},{<!>!>,<!!!>},<,,!>,<!!'!}!ueeueoaao{u>,<'i}}{!>},<">}},{<>}},{{},{{{{<u>}},<!>},<!!i'{!>,<!>,<<u{{!>"!>,<!!!o!>,<!!"e!>},<>},{}},{{{<,<!!!>!{!>},<<!!!>'!>},<o>,{<,!a<u!>}!!!!!>!!!>>}}},{{<}!>},<!>},<u'!>e<eo,!!!>!"!!ao!ua>}},{{<a!}'!>},<}'oa!oa!>},<!,a!>u!>a'e>},{{{<!!!!e!>{>},{}},<o>}}}}},{{{<iue!>},<>,<!><,u!!!!!>ae<{{>}},{{<!!!!,!>!>!!!!!>!!'!<!!oo!>,<!>,<!!i!!!>>},<,,!!}!}!>o">},{}},{{{<i!!eio{{!>,<}>},{<'uou!a{,'i!!!>!>o{>}},{{<"!>},<!!!!!!!>,>}}}}},{{{{{<'!><!>,<au!!!io!!!>!!!>},<!>,<!!!>!>},<!!!>}!!>},{<"!>},<!i!>},<,'!!{i!a!!!!!>a"!!!!a'u!!>}},{<},,!>},<e!!!>"!>},<<u>,{<>}}}},{{<,<!!!>}<!oi!>}'!>,<'i!>>,{<!{i!!!>uo!!oie>}}},{{{<u'{>}}}},{{{{{{<a!!>}},<a!!"'!!i,,!!uo!><e!!!>ui>},{{<i{o!!!>a!!!>u!!{ai>,<!>!!!i"!>},<a{}!>'!!!!''<ae!>a!!!>},<>}},{{<ea'e!>!ao!!!>>,<i!!!>!>!!!!!><u!>}!>a>}}},{{},{},{{<!!ue!>},<'>}}},{{{{{<!<<<,"o!>,<a<!>},<,>},{<u!!!!!"!!!!!!"!>},<!>!!<!!!>,<!a'!!}!!>}},{{<!>},<!>},<!!i{!!!>!>o!!"u!!o>},{{},{}}},{{{<"e"io!!i!>,<i!!!!o"',>},{{{<!>},<!>},<e!>!>},<!>},<!!,!!}<,<>}}}}}},{{<!!!>,<!!!'a!>,<,"!o!!!>!>'>},{<}e>}}}},{{{{{},<{o!>,<o{,"i,!!e!!e!>},<!!a}!>},<>},{<!>!>},<'!>},<i!>,<u!i'!!!>}!!!>!!,oo{>,<u!>},<,{i!>!>,<'u!!!>,<i>}},<"!>,<!!,,'!!!!i>},{{<u!>i">},{<'u'''!!!>e!>!!u'!>,<!a!"!!ua>,<"!}<u'eo!a!>,<"}!,}a"!>},<>}},{{<!>}e!!'!!!>>},{<!!{!>},<>}}}},{{{{{{{}},{<>}},{}},{{{{<!i{!{!!!>"a!!o!!!>'eo!>},<!>!o!>},<>,<a!"!>},<!!}!u!!<!!!!,a'<i!>,<!!"!{o>},<iu{!>,<!"!u<>},{<,i!>,<,}!>},<!><{!!'!>},<>,<!>!u!!!>!!!!",!>,<!{}i!!!>e!!e>},{{},<!>},<!>},<'!!'!!!>!>},<}<!!"!!!>'!>,<{>}},{},{{{<!!e}au",u!!!>}!!u,}!!!>'!!!!!>'!!!>>,<!>,<oa,!}"u!>!!o!!a>},{{<!>},<!!{'o!>oo!>!>!!'e!!u,>}}},{{}},{<!>,<"!!uu!>!!eu>}},{{{<!>},<u!o"'!!!>!!ue"ea!}}>,{{<!>'>}}},{{<!>},<!>},<i!!o!>},<ia}ee!!!!ao!>,<!>,<ua>,{<!!!!!>!!!>u,<!>,<e!!ea<>}}},{<'<!>ou'!ao,>,{<a!>,<!!!!i>}}},{<!>,<"!o!>,<,e!>,<<"!>,<",<a>},{}}},{{{<>}},{{},{}}},{{{<!>e!o>},{},{<{ua!>!>,<!}!!,!!!>i'<!!u!!{!>,<>,<!!!>>}},{{{{<!!!!!!!!u!!!>i!a!>!!!!i!!{<!!!!}!>,<!!oo<"a!!!!!>>},{<!!!>!!aau'!>},<!!a!!{!>},<a>}},{{},{<!>'a}!>,<!!!{!!!>"!,>}}},{{{{{<"<<!>},<o{oao{!!!>!}{'!>},<>},<,e,!!!>,<!o!ioiu!!<!>,<e>},{<!u<i,!>"}!!!>!>>}},<'eoa{'>}},{{<e>},{<>},{<}!>!!o!ue,o{"!!e'!>!!<!!!>>,{<>}}}},{{{{<!>},<!!a!>,<!!!>!!>},<!>"e!a<a"{!>,<!i}<a!>,<}!>>},{<!!e>,{<o{}!i!!<{!!!!{!o'<!>},<!>},<o>}},{{<!!o!>!!!>!>>}}},{{{},{<e,o!!!>!>"{'u!{e!>},<!o!>},<!!'!!e>}},{{<!!!>"!}!!!>o!ao'e!}!>!>>}},{<e'!>},<u}!>},<!>},<{<''!!!>u!i'!!!>!>},<!>i>,{{},<!>},<eua,{!!!!"!>},<u!>},<!>,<!,"oi>}}},{{<i,{"}!>,<e,e"!!!>}}i!{!!!!!>,<>,{}},{{<e!!!>!>,<,!>,<a}u!>!>i!>},<!!a{>},{<u}{}}!!!!!>!!!>{<ae!>,<oo!>,<a{>}},{<"<'<!!'"o!!!!i!!i!>},<!>,<!o!!e!>},<!<!!!a>,<!>u!!'!!!>!>,<{{uui!>,<"!!"!!>}}},{{{<e!>},<!!"i!!{ee!!,euu"<!>,<u!!!>!!u,>},{{<!!!!!><'!,!>ee!>},<<!>,<oa!>,<!!!>>}},{{<u!!!!!>{{i!>,<{oi!><<>},{{<'<o"!!eo!>!!!>},<>}}}},{{{<!>!'!>,<!!!>e!>!!!u,>,{<!>"u!!a{!>,<>}},{<e!>},<e!u",{{ei!>!>,<!!!"ui,>,{<!!!><!!!!!><}!!"eo!!!">}}},{{{<{,!!i!!!!!aa!>,<!>,<>},<ei!>,<oo}!!!><!>,<,!>},<o<!!!>!!!>!u!!!>,>},{{{{<i<,}ii>},<oa!>,<"eu!!'!!!>!!!!o!!!!!>,<!!!>>},{{{<,>},<'oa!!!!u}e!!}}!>,<ea{"!>!!,>}}},{{<u!!"<'>},{<!>},<}!!>}},{{<!>,<>},{<!e!!e!!o{u!>i!>,<',}e"'>}}},{<!!!>e!!}e{}'}!!>,{}}}},{{{{{<aaae"'!!"<u!>},<>}},{<!>u!!au!>,<!!<<'>,<<,o!!!!!>iie>},{{{<uo{}!>,<!>},<>,{<!ie!!o<<!!!!!>!!!!!!>}},<o!!!u!!!>i}<!!!>},<{!>,<!u!!!>,<e'!!{ieu>}}}}},{{{<!!{a!>i{u<}i<!!"!!!>!!,>},{{{}},<{a!e!>o!<!>"o>}},{{{<'!!u!!u>},{{},{<!><!e'e!!"!>>}}},{{<!!!!}{a!!!>!!au{i>},<{e!>!>},<!>},<}o>},{{<!<!>,<}e!e'>}}}}}}},{{{{<e'!i!><!>,<!!'!!<a!>,<,!!!>>}},{<!!<!>},<'iu>,{<e{!u!!!>},<<>}}},{{{<<{,!!,!!u!!}}!!u!!!>i>},{<ae!!!>'o{o"{!!!<,!!}u!!!>!u!!>}},{<}'!!!>!>"!!'},}i!>,!>,<'">}}}},{{{},{{},{<eeuo!>},<>}},{{<'"!!<e!>,<>,<a'!>,<!!!>},<!!aa!!!>eu!!!>,<i!!!>>},{}}},{{{<i!>!!o!!'>,<!>!aa'!>},<',{>},{}}},{{{{},<{!!!>,<!>,>}}},{{{{<!!!>a'!!u!>,<a}}!>,<!}!>!>,<>},<<e!>,<!>},<!,}}"!<!!!!!>!"u>}},{{}}}}},{{{{<!}!!"o!>},<!!'i}!>},<!>'"ui{a{>},{<!>},<e!!!>oe!!!><<<,<',!ee!!!!o{>}},{{<!!o'!>,<!!!e}i!}>,<!>o!!'<oa>},{{}}}},{{{<!!"'e{u}>},{{},{<ue'!>!!!!!!}!,'{i,,!,}!>,<!!!>!>,<>}}},{{},{{{<<e!>,<}a!>,<>}},{<!"!!!>!>!}{ii!>},<{"e!>},<'aooe>,<!>!>,<!!<i"!>,<!>a!!!!oa,o>},{<!!!>},<ei!>,<>,<!>},<''i!>!>,<u!!!!}!>>}}},{{},{{<a!!!>!ia!!o!!!>},<!!!>},<!'!!!>ia>,<o{!>oa!!!>}'"!!a}{!>},<!!!!!>!>,<'}>}}},{{{<"!>,a,!!!>ui!!!!">},<{<!!e!!!>i!!a,!!!>'>},{<!>},<!"e"}ue!>,<!!}}!!a!>},<!!'}!>,<!<"u>,<<"!!!>,'{i"u!>,<ou,eo>}}}},{{{{{},{{{<!>},<!{!>!!ou}!>,<i!iu!>},<<!!uo<>},<<!u,}a!>!{>},<{!!u<!>,<<!>e'!!!{<e!u!!!>!!a!>,<,>},{}},{}},{{{}},{{{{<!>},<u{"!!!!>},<!>},<e!!e!>},<!>,<io!!iau!>!!!!!>'!u>},<e!>,<!>,<<e!<u,}e"!>,<!!!>!>!!>},{{<}i!!>},{<!!"!!,,,!>,<u"!!!>,<eo}a"!>,e'},>}},{}},{{{<!!!>,<a>}},{{{{},<e!!"!!i!!'!>"!!!>!>,<>},{<<}u!>},<o'!"!!u!!!>>},{{<}!!!>},<,o!>ai{"!>e!!!>},<a>},<<iaa<!>}},"a!>},<eu>}},{{{<!!!!o'}u!!u!!'e!{!!e!>},<{!{}i!>,<u!>,<>}},<ia!!!!!!!>!>},<!!!>'>},{<!>,<<ee>,{<}!!u{ea}!<e">}}},{<>,<!!!!o!!!>}<oa"i!>>}},{{},{{{{<<!!{!!"!>,<}!!<!"i!>,<,a,i>},{<{!'<{a!>"!>},<ue<>}},{<!!!>,<,u!>!!'i!'!>},<,,>,{<,!,!u!>"!>},<{!>},<}a}'!,>}}},{{<!>!>},<!>{!!!>e!!e!>},<!!<eo!!o'!!!!!>!>,<>},<o>},{{{<!>},<u!!!>!!!>'<{<!>!!'e!>},<a!!!>u}oo>}},{<ee'a,'{!!!!!o!ooi!uu>,{<au!uu,!!}"!>,<ie<>}}}}}},{{{<}e<!>,<o!au!>},<}!!!>!!!>a}u!>},<!!!>,'}>},{{{<i!>!!!>,<!>!,!>,!eu<a}>},<!'!!!!'!!!>{,>},<u}i!>>}},{}},{}},{{{{},{<,i!!!>!!}!!!>u!!!>!>">}}},{<!{<!!!>,!>,<!>!>},<i!>},<}!!!i>,<>}},{{{<!>,<!>},<',i}}>},{{<{i!>>}},{{<ei!>,<!>!>,<a!!!>!{!>},<>,{<ae"'>}},{{<!!!>!>},<!>},<!!ia!!"'"!!o!!!>!>,<}'!><!>},<"!!!>>,<<!!i!>,<!>e'!!!>!>},<uoui!!}u>},{}},{<o!>!!!>!>,<a}eii>}}},{{{{{}}},{{<!'!>},<au,!!!>">}},{<{oi}!>!>ai!>">,{<!>},<">}}},{{{<e!!{!>},<>},{}}}}}}}},{{{{<e<!!!>!!"o!>},<>},{{{<u!!,,!>},<o!!!!,!!!>},<aii>}},<}{!{a!>uo!>>}},{{{{}},{<e'{e>}},{{<!>!!uo"o!!i'ae!>},<!!!>,!>,<i!!'>,<!>!!!>u>},{{},{}}},{{{{<!!!>'!>,<,i!!!>>,<!"e>},{}},{{{<o!!!>},<!!!>!>,<!{a!>e{,!>,<!<o{!>},<!!{>},{{{<''<!!!o!>,<!>i{!!!>}!>},<"a!!!a!>,<!!!!!"'a>}},{{<,!!!>,<!!<'}!>,<!!!>{""uu!oo!!e,!>,<'!!a>},{<,",!>,<>}},{<!!i!>,<!!!!!'!>!!!>"!!,<o!!{!><!>},<}!o>,{<,!>!'!>{uo!!!>>}}}},{{<o!!}!>,<"ooi>},{{<iiu,!!o!>,<aa!e<'>,<!!!>,<u!i{u!!!>},<!!!!!>,<!>},<o>},<!e,}'oe'i!>!>e>}}},{{<!><'!>,<i<i'!!!!'<!>},<aoa>},{{<!!!>>}},{{},{<e!!{'{>}}},{{{{}}},{{<e<{i!>},<,!!!>"!>'a!!''>,{<,!>},<!>,!!"!>!!!!!!!>"e!!o!!!>a<!!{!u!>,<>}},{{},{<!!"!,!!!i!!!>!!o!>,,{!<!!!>"a"u!">}}}}},{{{<a<>}},{{{<!><{!>},<oo!>},<}}!a{!!!!,!>>},{<!!!"'!!!>ueu!>,<!>,<!>},<e!!!><>}}}},{{{{<'a!>},<!!!>u!!!>!!!>},<!!'"}a>},<!!'{>}},{{{},{<!>!!!>!!,u<i!>!>},<,'!>},<i,>}},{{<,{a{""!>,<!e!!!>!!,!>}'<}>},{<o!>oa!>},<aa!!oe{!>">}}}}},{{{<{,u}u<}"!>},<!e>}}}}},{{{{{},{{{{<!>,<>},{}},{{<<>}},{{<o!e!!'<}!!!>iae!>,<>}}},{<>}}},{{},{{{<a'!>},<>},<!>!!!>o!!o!>,<>},{<<a!>},<>}}},{{{{<!>},<!!e,i!!!>,<u<!>},<o<'<!<!!o{!eo>}},{{<oo!>a"o!!!>u!>},<!a'!!!!!!'!i>},<!!"{"!!!><>}},{{<!>,<>},{{<!>!!!>ea!>},<'<{io>},<!!!>!>,<!!!!i{!!!>!}!>!!!>,",a<a{!e}>}}}},{{{{{{{{<!>,<!!''!>},<{!!{!!!>!!"!>},<a!,<u>},{{{{<>},<,<o!!!>">},{{{{<u!uu!!<!!!!}>},<!!!>,'a,{!!!!iie,!!!!>},{<}o'o!<!!!>u!!,<''!!!!>,{<}'"o,u!!!><u!!!>},<!!!>!}!!!>!!<">}}},{{}},{<!!!>"!>},<!>,<e{oi,>,{<!>!!!>!>},<!!,,!!}u!>!!!!!>,<"!!!>,<,!>,<ie}!>,<i{>}}}}},{{<u}a!>},<!!i!"<">},{{{{<{'{!<!>,<!!!>>}},{}}}}},{{<a!!!>>}}},{<!>,<!>,<!!!>"!>,<i!!u,}{>,<'}!!!"{!>},<!>},<!!!!i!>},<}a!>""!>,<!!!!!>u>},{<!>,!>,<ie<a!!!>u"!>,<>}},{{{}},{<}!!a!e!!!>,!!!!!>>,{<!>{,,!,!!o{}''!>},<!>,<!{"'oo!>>}},{{{{}},<!>},<}ai"!>},<!!{!,!{}''o!!{!!!>,>},{},{}}}},{{<!}a{i>},{{<}!!!>,<!>,!!!>"!"ieia}!>},<'!>,<i>,{<!>,!}!!!!o{a''!>!!!>>}},{<u!!a!'!!}i!!u'!!,,,!!!>{o,>,{<ae!>},<"u,!!!>},<i!!!!!>},<!>},<!!a!!>}}}}}},{{{<!!,i!!!!ie>,{<!>},<!>o!!!>!'}<oe!!",!!iu!!!>>,{<!!<!>a','"!a!!!>i!e{o!>!!'!>,<>}}},{{{},{<<<>,{{{<ai!!!>!!i{e}eia"!>},<'!>'!e>},{<<,!!>}}}}},{{{},{<,i<}<!!"!>}>}}}}}},{{},{{<'>},<!!!!!>!>},<}>},{{{<e!>e{<}!>,<<o>}},{<!>,<e<o!>!""!!!>au!>},<o!!!>{!!a}e{!!!>>}}},{{},{{<!!o!>},<i>,<!o!!oae"!!<!!>}},{}}},{{{{}},{<!>},<{,{{!',a>,<<,!>,<}!>},<!!e!>!!uu",i<i<u!!">}},{{{{<!!aoa!>},<e{}!>},<!,!!u}aa>},{}},{{{<!!!>i'!oa!a!!a}'}!!!>e}>},<<!>,<u'!!!!{!!"<!>,<!!!>}}{u!>,<<"!!>}},{{},{<i>}}},{{<',!!!>!!!>!>,<>,<i!>aeoao<<!>{!>,<>},{{<,u!!!!e!>>},{{{<u!>},<!>},<!>!>},<!!}{,i<!>!!!>""o<>}},{{<}>},<!>,<}!!!>},<!>,<i,{!>,<"uo!e!!<!!!>}!>,<>}}}},{{{<,!',u!<,!!"ie">}}}},{{{{<!!!><!!<ae<!>>},{}},{{{{{<ui!>!>,<!>{,e!!ee!>,<e!i>,<!!!!!>{aio!!},>},<!!<"!!!!!!a<ou,>},{<!!,!!!!!o!>!>,<!!e!!!>,!>,<!!aaii!>'<!!!>!>>,<,!{!!!!!>"io>}}}}},{{<<'!u!>!!'{!!,!!!!i!>}!>!!a,!!!>,<a>,<!!!>!!!>"!!!>'}!!<<>},{{<oi<!,<!>},<<e!!>},{<"a}!>>},{<o!>,<<"i<!!!!!>e'e}i>,{}}},{{<oei!!,!!!>},<,}{!!o>}}},{{},{}}}}},{{<u!!!>oo>,<'e<"!!>},{{<!!!>{>}},{{{{<}o!!!!"{i'!!!!i>},{<u!'}<!!i!!i,i!!!>!a!!e">}}},{<!>},<!>,<'u>}}},{{{{<{{i!>},<>}}},{{<o!!a<>,<!!}!!{!!!>,<{!!!>,<!!u!>,<!!!>,<!>>},{<{o!!<a"<!>,!!!>,<!>!!,auo}!!!>!!}!!">,<!!<,">}},{{<{!>ei'ie!>},<}!!{e!>},<!>},<!!!><o>,<ie,},!>},<{!!<!!!>e">},{<!>"!!>,{}},{<{i{u!>},<o!>},<!>},<>,<{!!!!!>!!i!!!!!>!!"{!>},<<<'o>}}}},{{{{{<ei!>},<!!!>!!!!ia{u!!a}}i"!>},<ii>}},{{}},{<!i''!!!>!!}!!'!!i!a"!!>,<i}!!"aa!!!>!>},<!>!ii!!!>u,}>}}},{{{<u!!!>{'e{ai"!!}!>},<<!!!!!>e!!!!!>!>,<">,{<!!!!!'}!>,<'!!!>}"<'!!!!!>o!!!>i<"<>,{<e!>{!!!>}!>,<}>}}},{{<u>},{<i!!e!!e!!!>},<!!"e'{>,{<!!e!<>}}}},{{<u>}},{{},{<!>},<!!!!,'!>"ie!>},<'u>,{<!>"e!><{}!>,<!>},<!>},<!!!>}u"i<!!aa{>}},{{}}}},{{<!a!"u'"!!{!>,<!!,!>oe!>,<>},{{<u!!!>!!!>i!!!>},<a,!>!>,<{!!,i!>},<!>},<>,{<{!>,<{!!!>,<{<o>}},{{<i"!'ai"!!oa!>,<e!!"!>},<!!!>!>!!"!!!>!>!!{>,{<!"!a!!!>!>!a!!u>}},{{{<e!!"<u'!!!!!i!!'<!!!>,ai!!}!!!>!>},<!!!>,<>},<!>,<ii,!>}!>},<>}},{<!!!>},<>,{<au!>}!!,u>}}},{{{<!!!>!>},<!>,<!>,<!o!>,<!!!!i!a!!"i>}},{<i!!i!!!>>},{{<u!!ai!oau'a,'{u>},<!!"!!!!>}}}}},{{{{{<a!>u"}""!ei<}o<!>,<>,<'>},{{{<>}},<!>,<!>},<}!{,!>,<!!{!{!!u<!!!>!oo>},{{}}},{<u!!!>!!'u,!!o"!>,<}i">},{{{<!>,<",'!>},<"{ai!!',!>a>}},<i!!!>},<i!>},<ei!{!!<{!>},<'!>,<{!!!'{o<ue>}},{{{<io!>!!!>},<},io!>,<}!!a}o!>!!!>,!!!'>},{{<!!!>!!!>"o>},<'!!}>},{{{<!>">}},{<!!!>e!>,<'{!>}'!<u>,{{}}}}},{{{{{<,!>},<!,'e'!>,<i!"<i!>aue'}>}},<!u'!!a!>"!>},<u!>,<!"<!>,<i!>},<!>},<!!oa>},<!>},<o{!>},<>}}},{{},{{<!>},<!>u"},!><<a!i!!u>},{<u,a!!<e<{>},{<!>},<!>,<}<u!!!>'>,{<u<}!>},<e!><u!!!!!>!>!>},<>}}}}},{{{{<!!ae>},<>},{{{<!>},<!>},<e'!!u!>,<!!!>!!!>{',iou>}},{{<"{{!!!>},<'}i!!a!!!>!>,<i!<>},{{<>},<!!!o>}}},{{}}},{{{<!>},<!!!>u!!,!!!!!><>}},{{<}!!"!>},<!>},<!!a!!!>a!!!>!!!>a!>},<"iu>},{<"<<!!{!!!>"!!a>,{<!>},<!>,<}o!!!!!>"!>},<!!eua}ie>}}}},{{{<!>!>,<ii!!e!e'{i!!oo!>},<!!!>}{i<u>},<!!<!!}"!!!>a"ui}<>},{{<,!>,<iia'o!"!>!>,<'u!!!}e}e>},<!>},<i!>},<eu!!!>!>!ao!!!>'o!>,<!i{!>,e>},{{{<!!a"!!<!>,o'>}},{{{<i!>>}},{{<<<!!!o!!,,o<ai>},<!>,<e,!!!>,'>}}}}},{{{<',!>u<}!!u'!>},<ai!!'>},{}},{{<<u!!!>!!!>{!!!>,!>,<!>},<!}!!!>!!!>>},{{<}",!>},<!>,!',!>!!<>}}},{{{{<{>},<!!!!<{!!!>>}},{{},{<,<uu'{">}}}},{{{{{<!!!>},<!!}>},<!>i!>!!!!!>!!"!>},<}!!!{!',o>},{<!!!>a!!!!!>},<!><o'{!>}!!<"!>},<!>},<!a>}},{{<!u'}!!}!!!<,a"a!>,<u!!">}}},{{{<i!>},<!!'}>,<<"u!>!>!>},<!!!>e!!!>u}>},{<!>},<"!>,<o!>},<!!u<}>},{<e,oi'!">,{{<}"!!!>},<e!!!>a!!!!!><e!!!!!!!>}!'i!o>},{<o!!"eu<u,!!e!!!!!!!e!"a!',!!!<ee{!!"o>}}}},{{{{<!>,<">},{}},{{}},{{{},{<!!>}},{{<{a!!!>,aa!!!>!>},<!>,<}}!!!>!>},<!!'!!!"au>},<!!!>!}!!!>,<a'!>o'}!u!>,<',!!oe!!"!!!!>},{{{{<!!a<}!!",,!iua!>},<!>",a'>,<!e>}},<{!!!>!i!!!!''a!>},<!!!>!!u,e,'>},<!>oi!"!>,<!>},<,o"e"o"!>,<!>>}}},{{<i"'!!}"}!!"u{!{,'u!!>,{<'i!!ea>}},{{<>},<!>,<!}!o!>,<"}}!>!>o>},{{<o'!!!!{>}}},{{{<o,'!!!>"<!>},<!!"ie,{'{!>},<,a>}},{{}}},{{{<o'!!}a!!>,{<u!>{u{uu!'!>,<i!!!!e!>!>},<<!!!>,<a,a>}},{{<e!!!!"'!>},<o!><>},<!!i!!!>!!!!!><o>},{{{<"u!!a!>},<}!!!>{!>,<>},<,{!!a!!>},<e<!>o<,!!!>i!!!>!!!>},<}i!>},<!>""!!>}},{{{{{{<{>}},{{<oi,'!>},<>},{{<!!!e!!'e!e!!e,!,!>!!!!!>>}}},{{<!!!>!!!!!!!>,<<a,aa!>},<i>,{{<'!!!>!}!!'a>}}},{<'!>,<e>}}},{{<!>>},<o!>},<'e!!,!>,<!>a<!{>}},{{<!{!!'!!!>},<u!,u{,!!i!e!!'!'!>!!!>oi>,<!u!!!>!!!!!>,<!!"!>!!!!e,!!<!>,<!!!>i>}},{}},{}},{{},{<!<}<e!>,<!!!>>,{<!>},<!>},<!!!>!>,<'<{',e>}},{<!>u'}!!!>ui!!}">,<!!e!<!>,<u!ie!!!>!>>}}}}},{{},{{{{},{{<>},{}}}},{{{<"}!>!!!>>}},{{{<<''!>,<u<"!o!!!>>},{}},{{<!!!>'"<!>},<!!!>,<!>,<i!!!>,!!!>!>},<>,{}},{<,{e!!!!!>},<>,<a'!>},<!!}!!!>>},{<>,{}}}}},{{{<<{>}}}},{{{<!>}i{!>},<!>!!!>},<''!>,<u!!u>},<{i'"!!!>!!!!!>!>!!!>!!i>}},{{{},{{<"!>,<!!!!!!!>,{{!!ue}!>>},{<!!}!>,<{!>'!>},<o{<!>},<!!!>",,!!u!!"o>}}}}}},{{{<!>,<a'i!>,<>,<!!{,<!>},<}e>},{{},{<,!!e>}},{<!!!>,<!>,<'e},!!!>}!>ei{}}!!'{!'>,<,<o,!,iu"}ue>}},{{<a!>"eo{!>,<,!>,<!!!!a!>,<'aai!>!>},<i'>},{{{<i!!!"{i!>,<!>,<!>},<>},{}},{{{{{<!ao!,a}!"!!!ee!>}!!!>>},<a,!>,<,!>},<a!>,<<"!!'">}}},{<!!'!!i!>!>,<>,{}}}},{<o!>},<!'{!>!o!>},<}!!}a!!!>>}}}},{{{{},<o{iu}"e!!!>,!!"o!>},<!!!>"!!a!>},<<!!<,>},{<,>,{<!>},<!!'<"i!!}!>},<!u<o!!!!!>,<>,{<u<,!!a"<!>,<!!!o!!aa}i}e}>,{}}}}},{{{{},{<!,u>}},{{<!!i!>!>,<!>},<,!>!>,<e!!u>,{<!'a!!!>,<!!!!,o!{!!i>}},{{{<!!"o!!!>i{"!>o!!!!!>>}},<<!!uu!>},<'ou<aeeaie!},i>},{{{<!!'a>},{<!>,<!!!>eae!>,<ou!!u}>,<>}},{<,i"u}!!'i'!!!>{!>},<!!{o!ii!>">}}}},{{<!>'ua"'>}},{{{},{{<!>!!!>a<'>},{<i!>,<!>,<!!!>,<!>},<a,,>,{<>}}}},{<,u!>aa{aeo!e,<>,{<!!>}}}}}},{{},{{{<''>,<}a!>},<ao!>},<{!!"!!}e}u!!a!>},<{!!u{>},{<ueo>,<}!<>}},{{<aeu!!i}!o!>},<!!!>i'}"{,<o>,{<ii!!!>},<>}}},{{{{<!>,<!!'o"o!!!>i{,i>}},{<<"o,o}!!!aa"e!!!>o>,<{!>,<ua{a>}},{{{{{},<'ui!!!>,<!!i>}},{<e<}!e!!u>},{<!!!a!!!>oo!!,!!!>,<o>}},{{<'uo}o!!<e!!!>},<u,"a>}},{{},{{},{<!>>}}}}}}}}"""
