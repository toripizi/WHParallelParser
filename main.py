
from api import MWApi
from bs4 import BeautifulSoup, element
from data import forbidden_tags, new_line_tags




class MWParser:
    def __init__(self, URL, cache_folder):
        self.api = MWApi(URL, cache_folder)

    def parse_wikicode(self, text):
        return self.parse_html(self.api.parse(text))

    def parse_html(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        root = soup.find("div", {"class": "mw-parser-output"})
        parsed = ParserJob(root)
        return parsed




class ParserJob:
    def __init__(self, root):
        self.root = root
        self.text = [""]
        self.data = []
        self.textLocation = 0
        self.process(root)

    def process(self, section):
        {
            element.Tag: self.processTag,
            element.NavigableString: self.processString,
            element.Comment: lambda a : None,
        }[type(section)](section)

    def processTag(self, tag):

        forbidden = False
        for forbidden_tag in forbidden_tags:
            if forbidden_tag["name"] == tag.name:
                match = True
                for name, value in forbidden_tag["attrs"].items():
                    if not (name in tag.attrs and tag.attrs[name] == value):
                        match = False
                if match:
                    print("Ignoring tag")
                    print(tag.name)
                    print(tag.attrs)
                    return


        print("tag")

        if tag.name in new_line_tags:
            if len(self.text[self.textLocation]) > 0:
                self.textLocation += 1
                self.text.append("")

        obj = {"tag": tag.name, "attrs": tag.attrs, "start": [self.textLocation, len(self.text[self.textLocation])]}

        for child in tag.children:
            self.process(child)

        obj["end"] = [self.textLocation, len(self.text[self.textLocation])-1]

        self.data.append(obj)



    def processString(self, string):
        if string == "\n":
            return
        str = self.fixString(string)
        self.text[self.textLocation] += str


    def fixString(self, string):
        string = string.replace("\r\n", " ")
        string = string.replace("\n", " ")
        while "  " in string:
            string = string.replace("  ", " ")
        return string




parser = MWParser("https://en.wikipedia.org/w/api.php", "C:\\Users\\Kajetan\\Desktop\\cache\\")
parser.parse_wikicode("'''asd'''")

output = parser.parse_html('''<div class="mw-parser-output"><style data-mw-deduplicate="TemplateStyles:r8034721">.mw-parser-output .infobox-subbox{padding:0;border:none;margin:-3px;width:auto;min-width:100%;font-size:100%;clear:none;float:none;background-color:transparent}.mw-parser-output .infobox-3cols-child{margin:auto}.mw-parser-output .infobox .navbar{font-size:100%}body.skin-minerva .mw-parser-output .infobox-header,body.skin-minerva .mw-parser-output .infobox-subheader,body.skin-minerva .mw-parser-output .infobox-above,body.skin-minerva .mw-parser-output .infobox-title,body.skin-minerva .mw-parser-output .infobox-image,body.skin-minerva .mw-parser-output .infobox-full-data,body.skin-minerva .mw-parser-output .infobox-below{text-align:center}</style><style data-mw-deduplicate="TemplateStyles:r8087921">.mw-parser-output .ib-country{border-collapse:collapse;line-height:1.2em}.mw-parser-output .ib-country td,.mw-parser-output .ib-country th{border-top:1px solid #a2a9b1;padding:0.4em 0.6em 0.4em 0.6em}.mw-parser-output .ib-country .mergedtoprow .infobox-header,.mw-parser-output .ib-country .mergedtoprow .infobox-label,.mw-parser-output .ib-country .mergedtoprow .infobox-data,.mw-parser-output .ib-country .mergedtoprow .infobox-full-data,.mw-parser-output .ib-country .mergedtoprow .infobox-below{border-top:1px solid #a2a9b1;padding:0.4em 0.6em 0.2em 0.6em}.mw-parser-output .ib-country .mergedrow .infobox-label,.mw-parser-output .ib-country .mergedrow .infobox-data,.mw-parser-output .ib-country .mergedrow .infobox-full-data{border:0;padding:0 0.6em 0.2em 0.6em}.mw-parser-output .ib-country .mergedbottomrow .infobox-label,.mw-parser-output .ib-country .mergedbottomrow .infobox-data,.mw-parser-output .ib-country .mergedbottomrow .infobox-full-data{border-top:0;border-bottom:1px solid #a2a9b1;padding:0 0.6em 0.4em 0.6em}.mw-parser-output .ib-country .infobox-header{text-align:left}.mw-parser-output .ib-country .infobox-above{font-size:125%;line-height:1.2}.mw-parser-output .ib-country-names{padding-top:0.25em;font-weight:normal}.mw-parser-output .ib-country-name-style{display:inline}.mw-parser-output .ib-country .infobox-image{padding:0.5em 0}.mw-parser-output .ib-country-anthem{border-top:1px solid #a2a9b1;padding-top:0.5em;margin-top:0.5em}.mw-parser-output .ib-country-map-caption{position:relative;top:0.3em}.mw-parser-output .ib-country-largest,.mw-parser-output .ib-country-lang{font-weight:normal}.mw-parser-output .ib-country-ethnic,.mw-parser-output .ib-country-religion,.mw-parser-output .ib-country-sovereignty{font-weight:normal;display:inline}.mw-parser-output .ib-country-fake-li{text-indent:-0.9em;margin-left:1.2em;font-weight:normal}.mw-parser-output .ib-country-fake-li2{text-indent:0.5em;margin-left:1em;font-weight:normal}.mw-parser-output .ib-country-website{line-height:11pt}.mw-parser-output .ib-country-map-caption3{position:relative;top:0.3em}.mw-parser-output .ib-country-fn{text-align:left;margin:0 auto}.mw-parser-output .ib-country-fn-alpha{list-style-type:lower-alpha;margin-left:1em}.mw-parser-output .ib-country-fn-num{margin-left:1em}</style><table class="infobox ib-country vcard"><tbody><tr><th colspan="2" class="infobox-above adr"><div class="fn org country-name">Republic of Poland</div><div class="ib-country-names"><span title="Polish-language text"><i lang="pl">Rzeczpospolita Polska</i></span>&nbsp;&nbsp;<span class="languageicon" style="font-size:100%;font-weight:normal;">(<a href="/wiki/Polish_language" title="Polish language">Polish</a>)</span></div></th></tr><tr><td colspan="2" class="infobox-image"><div style="display:table; width:100%;">
        <div style="display:table-cell; vertical-align:middle; padding-left:5px;">
            <div style="padding-bottom:3px;"><a href="/wiki/File:Flag_of_Poland.svg" class="image" title="Flag of Poland"><img alt="Flag of Poland" src="//upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/125px-Flag_of_Poland.svg.png" decoding="async" width="125" height="78" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/188px-Flag_of_Poland.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/250px-Flag_of_Poland.svg.png 2x" data-file-width="640" data-file-height="400"></a></div>
            <div><a href="/wiki/Flag_of_Poland" title="Flag of Poland">Flag</a></div>
        </div>
        <div style="display:table-cell; vertical-align:middle; padding: 0px 5px;">
            <div style="padding-bottom:3px;"><a href="/wiki/File:Herb_Polski.svg" class="image" title="Coat of arms of Poland"><img alt="Coat of arms of Poland" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Herb_Polski.svg/85px-Herb_Polski.svg.png" decoding="async" width="85" height="100" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Herb_Polski.svg/128px-Herb_Polski.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Herb_Polski.svg/170px-Herb_Polski.svg.png 2x" data-file-width="3158" data-file-height="3716"></a></div>
            <div><a href="/wiki/Coat_of_arms_of_Poland" title="Coat of arms of Poland"> Coat of arms</a></div>
        </div>
    </div></td></tr><tr><td colspan="2" class="infobox-full-data anthem"><b>Anthem:</b>&nbsp;"<a href="/wiki/D%C4%85browski%27s_Mazurka" class="mw-redirect" title="Dąbrowski's Mazurka">Mazurek Dąbrowskiego</a>"<br><span style="font-size:85%;">Mazurka dąbrowskiego"</span><br><div class="center"><div class="floatnone"><div class="mediaContainer" style="width:220px"><div class="mwPlayerContainer k-player" style="width: 220px; position: relative; height: 20px;"><div class="videoHolder"><div class="mwEmbedPlayer" id="mwe_player_0" style=""><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkqAcAAIUAgUW0RjgAAAAASUVORK5CYII=" class="playerPoster" style="position: absolute; inset: 0px 0px 0px 100px; height: 20px; width: 20px;"></div><div title="Play clip" class="play-btn-large" style="left: 50%; top: 50%; margin-left: -35px; margin-top: -27.5px;"></div></div><div class="ui-state-default ui-widget-header ui-helper-clearfix control-bar block" style="height: 20px;"><div title="Player options" class="ui-state-default ui-corner-bl rButton k-options"><span>Menu</span></div><div class="ui-slider ui-slider-horizontal rButton volume-slider ui-widget ui-widget-content ui-corner-all"><div class="ui-slider-range ui-widget-header ui-slider-range-min" style="width: 80%;"></div><a class="ui-slider-handle ui-state-default ui-corner-all" href="#" style="left: 80%;"></a></div><div title="Volume control" class="ui-state-default ui-corner-all ui-icon_link rButton volume_control"><span class="ui-icon ui-icon-volume-on"></span></div><div title="Timed text" class="ui-state-default ui-corner-all ui-icon_link rButton timed-text"><span class="ui-icon ui-icon-comment"></span></div><div class="ui-widget time-disp">0:00</div><div title="Play clip" class="ui-state-default ui-corner-all ui-icon_link lButton play-btn"><span class="ui-icon ui-icon-play"></span></div></div></div></div></div></div></td></tr><tr><td colspan="2" class="infobox-full-data"><a href="/wiki/File:EU-Poland.svg" class="image" title="Location of &nbsp;Poland&nbsp;&nbsp;(dark green) –&nbsp;on the European continent&nbsp;&nbsp;(green &amp;&nbsp;dark grey) –&nbsp;in the European Union&nbsp;&nbsp;(green)&nbsp; —&nbsp; [Legend]"><img alt="Location of &nbsp;Poland&nbsp;&nbsp;(dark green) –&nbsp;on the European continent&nbsp;&nbsp;(green &amp;&nbsp;dark grey) –&nbsp;in the European Union&nbsp;&nbsp;(green)&nbsp; —&nbsp; [Legend]" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/9b/EU-Poland.svg/250px-EU-Poland.svg.png" decoding="async" width="250" height="210" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/9b/EU-Poland.svg/375px-EU-Poland.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/9b/EU-Poland.svg/500px-EU-Poland.svg.png 2x" data-file-width="2045" data-file-height="1720"></a><div class="ib-country-map-caption"><div style="text-align:center;font-size:11px;line-height:1.15em;"><span style="font-size:11px;">Location of <span style="font-size:2px;">&nbsp;</span><a class="mw-selflink selflink">Poland</a><span style="font-size:8px;"><span class="nowrap">&nbsp;&nbsp;</span></span>(<span style="font-size:9px;">dark green</span>)</span><p style="width:250px;font-size:11px;text-align:left;margin-left:1.2ex;margin-top:0px;margin-bottom:0px;line-height:1.15em;">–&nbsp;on the <a href="/wiki/Europe" title="Europe">European continent</a><span style="font-size:8px;"><span class="nowrap">&nbsp;&nbsp;</span></span>(<span style="font-size:9px;">green &amp;&nbsp;dark grey</span>)<br>–&nbsp;in the <a href="/wiki/European_Union" title="European Union">European Union</a><span style="font-size:8px;"><span class="nowrap">&nbsp;&nbsp;</span></span>(<span style="font-size:9px;">green</span>)&nbsp; —&nbsp; [<span style="font-size:10px;"><a href="/wiki/File:EU-Poland.svg" title="File:EU-Poland.svg">Legend</a></span>]</p></div></div></td></tr><tr><td colspan="2" class="infobox-full-data"><a href="/wiki/File:Un-poland.png" class="image" title="Location of Poland"><img alt="Location of Poland" src="//upload.wikimedia.org/wikipedia/commons/thumb/6/69/Un-poland.png/250px-Un-poland.png" decoding="async" width="250" height="195" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/6/69/Un-poland.png/375px-Un-poland.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/6/69/Un-poland.png/500px-Un-poland.png 2x" data-file-width="3038" data-file-height="2364"></a></td></tr><tr><th scope="row" class="infobox-label">Capital<div class="ib-country-largest">and largest city</div></th><td class="infobox-data"><a href="/wiki/Warsaw" title="Warsaw">Warsaw</a><br><style data-mw-deduplicate="TemplateStyles:r7427044">.mw-parser-output .geo-default,.mw-parser-output .geo-dms,.mw-parser-output .geo-dec{display:inline}.mw-parser-output .geo-nondefault,.mw-parser-output .geo-multi-punct{display:none}.mw-parser-output .longitude,.mw-parser-output .latitude{white-space:nowrap}</style><span class="plainlinks nourlexpansion"><span style="white-space: nowrap;"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/5/55/WMA_button2b.png/17px-WMA_button2b.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/55/WMA_button2b.png/17px-WMA_button2b.png 1x, //upload.wikimedia.org/wikipedia/commons/thumb/5/55/WMA_button2b.png/34px-WMA_button2b.png 2x" class="wmamapbutton noprint" title="Show location on an interactive map" alt="" style="padding: 0px 3px 0px 0px; cursor: pointer;"><a class="external text" href="//geohack.toolforge.org/geohack.php?pagename=Poland&amp;params=52_13_N_21_02_E_type:city" style="white-space: normal;"><span class="geo-default"><span class="geo-dms" title="Maps, aerial photos, and other data for this location"><span class="latitude">52°13′N</span> <span class="longitude">21°02′E</span></span></span><span class="geo-multi-punct">&#xFEFF; / &#xFEFF;</span><span class="geo-nondefault"><span class="geo-dec" title="Maps, aerial photos, and other data for this location">52.217°N 21.033°E</span><span style="display:none">&#xFEFF; / <span class="geo">52.217; 21.033</span></span></span></a></span></span></td></tr><tr class="mergedtoprow"><th scope="row" class="infobox-label">Official&nbsp;languages</th><td class="infobox-data"><a href="/wiki/Polish_language" title="Polish language">Polish</a></td></tr><tr><th scope="row" class="infobox-label">Spoken languages</th><td class="infobox-data">
<dl><dd>Polish</dd>
<dd>Lithuanian</dd>
<dd>Kashubian</dd>
<dd>Czech</dd>
<dd>German</dd>
<dd>Romani</dd>
<dd>Ukrainian</dd>
<dd>Hungarian</dd>
<dd>Slovak</dd>
<dd>Belarusian</dd>
<dd>Russian</dd>
<dd>Romanian</dd>
<dd>Yiddish</dd>
<dd>Rusyn</dd></dl>
</td></tr><tr><th scope="row" class="infobox-label"><a href="/wiki/Ethnic_group" title="Ethnic group">Ethnic&nbsp;groups</a> <div class="ib-country-ethnic"> (2011<sup id="cite_ref-1" class="reference"><a href="#cite_note-1">[1]</a></sup>)</div></th><td class="infobox-data"><div class="plainlist"><ul><li>94.61% <a href="/wiki/Poles" title="Poles">Polish</a></li><li>0.28% <a href="/w/index.php?title=German_minority_in_Poland&amp;action=edit&amp;redlink=1" class="new" title="German minority in Poland (not yet started)">German</a></li><li>0.12% <a href="/w/index.php?title=Ukrainians_in_Poland&amp;action=edit&amp;redlink=1" class="new" title="Ukrainians in Poland (not yet started)">Ukrainian</a></li><li>0.12% <a href="/w/index.php?title=Belarusian_minority_in_Poland&amp;action=edit&amp;redlink=1" class="new" title="Belarusian minority in Poland (not yet started)">Belarusian</a></li><li>0.04% <a href="/w/index.php?title=Kashubians&amp;action=edit&amp;redlink=1" class="new" title="Kashubians (not yet started)">Kashubian</a></li><li>0.03% <a href="/wiki/Romani_people" class="mw-redirect" title="Romani people">Romani</a></li><li>0.02% <a href="/w/index.php?title=Lemkos&amp;action=edit&amp;redlink=1" class="new" title="Lemkos (not yet started)">Lemko</a></li><li>4.99% other</li></ul></div></td></tr><tr><th scope="row" class="infobox-label">Religion <div class="ib-country-religion"> (2011)</div></th><td class="infobox-data"><div class="plainlist"><ul><li style="white-space:nowrap;">87.6% <a href="/wiki/Roman_Catholicism" class="mw-redirect" title="Roman Catholicism">Roman Catholicism</a></li><li style="white-space:nowrap;">7.1% No Answer</li><li style="white-space:nowrap;">3.1% <a href="/wiki/Religion_in_Poland" title="Religion in Poland">Other Faith</a></li><li style="white-space:nowrap;">2.2% None</li></ul></div></td></tr><tr><th scope="row" class="infobox-label"><a href="/wiki/Demonym" title="Demonym">Demonym(s)</a></th><td class="infobox-data"><div class="hlist hlist-separated"><ul><li><a href="/wiki/Polish_people" class="mw-redirect" title="Polish people">Polish people</a></li><li><a href="/wiki/Poles" title="Poles">Pole</a></li></ul></div></td></tr><tr><th scope="row" class="infobox-label">Government</th><td class="infobox-data"><span class="nowrap"><a href="/wiki/Unitary_state" title="Unitary state">Unitary</a> <a href="/wiki/Semi-presidential_system" title="Semi-presidential system">semi-presidential</a></span> <a href="/wiki/Republic" title="Republic">republic</a></td></tr><tr class="mergedrow"><td colspan="2" class="infobox-full-data"><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r8034721"></td></tr><tr class="mergedrow"><th scope="row" class="infobox-label"><div style="text-indent:-0.9em;margin-left:1.2em;font-weight:normal;">•&nbsp;<a href="/wiki/President_of_Poland" class="mw-redirect" title="President of Poland">President</a> </div></th><td class="infobox-data"><span class="nowrap"><a href="/wiki/Andrzej_Duda" title="Andrzej Duda">Andrzej Duda</a></span></td></tr><tr class="mergedrow"><th scope="row" class="infobox-label"><div style="text-indent:-0.9em;margin-left:1.2em;font-weight:normal;">•&nbsp;<a href="/wiki/Prime_Minister_of_Poland" title="Prime Minister of Poland">Prime Minister</a> </div></th><td class="infobox-data"><a href="/wiki/Mateusz_Morawiecki" title="Mateusz Morawiecki">Mateusz Morawiecki</a></td></tr><tr style="display:none"><td colspan="2">
</td></tr><tr><th scope="row" class="infobox-label">Legislature</th><td class="infobox-data"><a href="/w/index.php?title=National_Assembly_(Poland)&amp;action=edit&amp;redlink=1" class="new" title="National Assembly (Poland) (not yet started)">National Assembly</a></td></tr><tr class="mergedrow"><th scope="row" class="infobox-label"><div class="ib-country-fake-li">•&nbsp;<a href="/wiki/Upper_house" title="Upper house">Upper house</a></div></th><td class="infobox-data"><a href="/wiki/Senate_of_Poland" title="Senate of Poland">Senate</a></td></tr><tr class="mergedbottomrow"><th scope="row" class="infobox-label"><div class="ib-country-fake-li">•&nbsp;<a href="/wiki/Lower_house" title="Lower house">Lower house</a></div></th><td class="infobox-data"><i><a href="/wiki/Sejm" title="Sejm">Sejm</a></i></td></tr><tr class="mergedtoprow"><th colspan="2" class="infobox-header">Formation</th></tr><tr class="mergedrow"><td colspan="2" class="infobox-full-data"><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r8034721"></td></tr><tr class="mergedrow"><th scope="row" class="infobox-label"><div style="text-indent:-0.9em;margin-left:1.2em;font-weight:normal;">•&nbsp;<a href="/w/index.php?title=Baptism_of_Poland&amp;action=edit&amp;redlink=1" class="new" title="Baptism of Poland (not yet started)">Baptism of Poland</a><sup class="reference" id="ref_b"><a href="#endnote_b">[b]</a></sup> </div></th><td class="infobox-data">14 April 966</td></tr><tr class="mergedrow"><th scope="row" class="infobox-label"><div style="text-indent:-0.9em;margin-left:1.2em;font-weight:normal;">•&nbsp;<a href="/w/index.php?title=Kingdom_of_Poland_(1025%E2%80%931385)&amp;action=edit&amp;redlink=1" class="new" title="Kingdom of Poland (1025–1385) (not yet started)">Kingdom of Poland</a> </div></th><td class="infobox-data">18 April 1025</td></tr><tr class="mergedrow"><th scope="row" class="infobox-label"><div style="text-indent:-0.9em;margin-left:1.2em;font-weight:normal;">•&nbsp;<a href="/wiki/Polish%E2%80%93Lithuanian_Commonwealth" title="Polish–Lithuanian Commonwealth">Polish–Lithuanian Commonwealth</a> </div></th><td class="infobox-data">1 July 1569</td></tr><tr class="mergedrow"><th scope="row" class="infobox-label"><div style="text-indent:-0.9em;margin-left:1.2em;font-weight:normal;">•&nbsp;<a href="/wiki/Partitions_of_Poland" title="Partitions of Poland">Partition of Poland</a> </div></th><td class="infobox-data">24 October 1795</td></tr><tr class="mergedrow"><th scope="row" class="infobox-label"><div style="text-indent:-0.9em;margin-left:1.2em;font-weight:normal;">•&nbsp;<a href="/wiki/Duchy_of_Warsaw" title="Duchy of Warsaw">Duchy of Warsaw</a> </div></th><td class="infobox-data">22 July 1807</td></tr><tr class="mergedrow"><th scope="row" class="infobox-label"><div style="text-indent:-0.9em;margin-left:1.2em;font-weight:normal;">•&nbsp;<a href="/w/index.php?title=Congress_Poland&amp;action=edit&amp;redlink=1" class="new" title="Congress Poland (not yet started)">Congress Poland</a> </div></th><td class="infobox-data">9 June 1815</td></tr><tr class="mergedrow"><th scope="row" class="infobox-label"><div style="text-indent:-0.9em;margin-left:1.2em;font-weight:normal;">•&nbsp;<a href="/w/index.php?title=History_of_Poland_(1918%E2%80%931939)&amp;action=edit&amp;redlink=1" class="new" title="History of Poland (1918–1939) (not yet started)">Second Polish Republic</a> </div></th><td class="infobox-data">11 November 1918</td></tr><tr class="mergedrow"><th scope="row" class="infobox-label"><div style="text-indent:-0.9em;margin-left:1.2em;font-weight:normal;">•&nbsp;<a href="/wiki/Invasion_of_Poland" class="mw-redirect" title="Invasion of Poland">Invasion of Poland</a>, <a href="/wiki/World_War_II" title="World War II">World War II</a> </div></th><td class="infobox-data">1 September 1939</td></tr><tr class="mergedrow"><th scope="row" class="infobox-label"><div style="text-indent:-0.9em;margin-left:1.2em;font-weight:normal;">•&nbsp;<a href="/wiki/People%27s_Republic_of_Poland" class="mw-redirect" title="People's Republic of Poland">Communist Poland</a> </div></th><td class="infobox-data">8 April 1945</td></tr><tr class="mergedrow"><th scope="row" class="infobox-label"><div style="text-indent:-0.9em;margin-left:1.2em;font-weight:normal;">•&nbsp;<a href="/w/index.php?title=History_of_Poland_(1989%E2%80%93present)&amp;action=edit&amp;redlink=1" class="new" title="History of Poland (1989–present) (not yet started)">Third Polish Republic</a> </div></th><td class="infobox-data">13 September 1989</td></tr><tr class="mergedrow"><th scope="row" class="infobox-label"><div style="text-indent:-0.9em;margin-left:1.2em;font-weight:normal;">•&nbsp;<a href="/w/index.php?title=2004_enlargement_of_the_European_Union&amp;action=edit&amp;redlink=1" class="new" title="2004 enlargement of the European Union (not yet started)">Accession to the</a> <a href="/wiki/European_Union" title="European Union">European Union</a> </div></th><td class="infobox-data">1 May 2004</td></tr><tr style="display:none"><td colspan="2">
</td></tr><tr class="mergedtoprow"><th colspan="2" class="infobox-header">Area</th></tr><tr class="mergedrow"><th scope="row" class="infobox-label"><div class="ib-country-fake-li">•&nbsp;Total</div></th><td class="infobox-data">312,678&nbsp;km<sup>2</sup> (120,726&nbsp;sq&nbsp;mi)<sup class="reference" id="ref_a"><a href="#endnote_a">[a]</a></sup> (<a href="/wiki/List_of_countries_and_dependencies_by_area" class="mw-redirect" title="List of countries and dependencies by area">69th</a>)</td></tr><tr class="mergedbottomrow"><th scope="row" class="infobox-label"><div class="ib-country-fake-li">•&nbsp;Water&nbsp;(%)</div></th><td class="infobox-data">3.07</td></tr><tr class="mergedtoprow"><th colspan="2" class="infobox-header">Population</th></tr><tr class="mergedrow"><th scope="row" class="infobox-label"><div class="ib-country-fake-li">•&nbsp;2018 estimate</div></th><td class="infobox-data">38,420,687<sup id="cite_ref-2" class="reference"><a href="#cite_note-2">[2]</a></sup> (<a href="/wiki/List_of_countries_and_dependencies_by_population" title="List of countries and dependencies by population">34th</a>)</td></tr><tr class="mergedbottomrow"><th scope="row" class="infobox-label"><div class="ib-country-fake-li">•&nbsp;Density</div></th><td class="infobox-data">123/km<sup>2</sup> (318.6/sq&nbsp;mi) (<a href="/wiki/List_of_countries_and_dependencies_by_population_density" title="List of countries and dependencies by population density">83rd</a>)</td></tr><tr class="mergedtoprow"><th scope="row" class="infobox-label"><a href="/wiki/Gross_domestic_product" title="Gross domestic product">GDP</a>&nbsp;<style data-mw-deduplicate="TemplateStyles:r6670383">.mw-parser-output .nobold{font-weight:normal}</style><span class="nobold">(<a href="/wiki/Purchasing_power_parity" title="Purchasing power parity">PPP</a>)</span></th><td class="infobox-data">2017&nbsp;estimate</td></tr><tr class="mergedrow"><th scope="row" class="infobox-label"><div class="ib-country-fake-li">•&nbsp;Total</div></th><td class="infobox-data">$1,110 trillion<sup id="cite_ref-imf-gdp_3-0" class="reference"><a href="#cite_note-imf-gdp-3">[3]</a></sup> (<a href="/wiki/List_of_countries_by_GDP_(PPP)" title="List of countries by GDP (PPP)">21st</a>)</td></tr><tr class="mergedbottomrow"><th scope="row" class="infobox-label"><div class="ib-country-fake-li">•&nbsp;Per capita</div></th><td class="infobox-data">$29,250</td></tr><tr class="mergedtoprow"><th scope="row" class="infobox-label"><a href="/wiki/Gross_domestic_product" title="Gross domestic product">GDP</a>&nbsp;<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r6670383"><span class="nobold">(nominal)</span></th><td class="infobox-data">2017&nbsp;estimate</td></tr><tr class="mergedrow"><th scope="row" class="infobox-label"><div class="ib-country-fake-li">•&nbsp;Total</div></th><td class="infobox-data">$509.955 billion<sup id="cite_ref-imf-gdp_3-1" class="reference"><a href="#cite_note-imf-gdp-3">[3]</a></sup> (<a href="/wiki/List_of_countries_by_GDP_(nominal)" title="List of countries by GDP (nominal)">23rd</a>)</td></tr><tr class="mergedbottomrow"><th scope="row" class="infobox-label"><div class="ib-country-fake-li">•&nbsp;Per capita</div></th><td class="infobox-data">$13,429</td></tr><tr><th scope="row" class="infobox-label"><a href="/wiki/Gini_coefficient" title="Gini coefficient">Gini</a>&nbsp;<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r6670383"><span class="nobold">(2014)</span></th><td class="infobox-data"><img alt="Positive decrease" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/92/Decrease_Positive.svg/11px-Decrease_Positive.svg.png" decoding="async" title="Positive decrease" width="11" height="11" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/92/Decrease_Positive.svg/17px-Decrease_Positive.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/92/Decrease_Positive.svg/22px-Decrease_Positive.svg.png 2x" data-file-width="300" data-file-height="300">&nbsp;32.08<sup id="cite_ref-4" class="reference"><a href="#cite_note-4">[4]</a></sup><br><span class="nowrap"><span style="color:orange">medium</span></span></td></tr><tr><th scope="row" class="infobox-label"><a href="/wiki/Human_Development_Index" title="Human Development Index">HDI</a>&nbsp;<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r6670383"><span class="nobold">(2015)</span></th><td class="infobox-data"><img alt="Increase" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/11px-Increase2.svg.png" decoding="async" title="Increase" width="11" height="11" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/17px-Increase2.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Increase2.svg/22px-Increase2.svg.png 2x" data-file-width="300" data-file-height="300">&nbsp;0.855<sup id="cite_ref-HDI_5-0" class="reference"><a href="#cite_note-HDI-5">[5]</a></sup><br><span class="nowrap"><span style="color:darkgreen">very high</span></span>&nbsp;·&nbsp;<a href="/wiki/List_of_countries_by_Human_Development_Index" title="List of countries by Human Development Index">36th</a></td></tr><tr><th scope="row" class="infobox-label">Currency</th><td class="infobox-data"><a href="/wiki/Polish_z%C5%82oty" class="mw-redirect" title="Polish złoty">Polish złoty</a> (<a href="/wiki/ISO_4217" title="ISO 4217">PLN</a>)</td></tr><tr class="mergedtoprow"><th scope="row" class="infobox-label">Time zone</th><td class="infobox-data"><span class="nowrap"><a href="/wiki/Coordinated_Universal_Time" title="Coordinated Universal Time">UTC</a>+1</span> (<a href="/wiki/Central_European_Time" title="Central European Time">CET</a>)</td></tr><tr class="mergedbottomrow"><th scope="row" class="infobox-label"><div class="ib-country-fake-li">•&nbsp;Summer&nbsp;(<a href="/wiki/Daylight_saving_time" title="Daylight saving time">DST</a>)</div></th><td class="infobox-data"><span class="nowrap"><a href="/wiki/Coordinated_Universal_Time" title="Coordinated Universal Time">UTC</a>+2</span> (<a href="/wiki/Central_European_Summer_Time" title="Central European Summer Time">CEST</a>)</td></tr><tr><th scope="row" class="infobox-label"><a href="/wiki/Left-_and_right-hand_traffic" title="Left- and right-hand traffic">Driving side</a></th><td class="infobox-data">right</td></tr><tr><th scope="row" class="infobox-label">Calling code</th><td class="infobox-data"><a href="/w/index.php?title=Telephone_numbers_in_Poland&amp;action=edit&amp;redlink=1" class="new" title="Telephone numbers in Poland (not yet started)">+48</a></td></tr><tr><th scope="row" class="infobox-label"><a href="/wiki/ISO_3166" title="ISO 3166">ISO 3166 code</a></th><td class="infobox-data"><a href="/wiki/ISO_3166-2:PL" title="ISO 3166-2:PL">PL</a></td></tr><tr><th scope="row" class="infobox-label"><a href="/wiki/Country_code_top-level_domain" title="Country code top-level domain">Internet TLD</a></th><td class="infobox-data"><a href="/wiki/.pl" class="mw-redirect" title=".pl">.pl</a></td></tr><tr><td colspan="2" class="infobox-full-data"><div class="ib-country-website"><b>Website</b><br><a rel="nofollow" class="external text" href="https://poland.pl/">poland.pl</a></div></td></tr><tr><td colspan="2" class="infobox-full-data"><div class="ib-country-fn"><ol class="ib-country-fn-alpha">
<li value="1"><span class="citation wikicite" id="endnote_a"><b><a href="#ref_a">^a</a></b></span>  The area of Poland, as given by the Central Statistical Office, is 312,679&nbsp;km<sup>2</sup> (120,726&nbsp;sq&nbsp;mi), of which 311,888&nbsp;km<sup>2</sup> (120,421&nbsp;sq&nbsp;mi) is land and 791&nbsp;km<sup>2</sup> (305&nbsp;sq&nbsp;mi) is internal water surface area.<sup id="cite_ref-CSO_2008_6-0" class="reference"><a href="#cite_note-CSO_2008-6">[6]</a></sup></li><li value="2"><span class="citation wikicite" id="endnote_b"><b><a href="#ref_b">^b</a></b></span>  The adoption of Christianity in Poland is seen by many Poles, regardless of their religious affiliation or lack thereof, as one of the most significant events in their country's history, as it was used to unify the tribes in the region.<sup id="cite_ref-7" class="reference"><a href="#cite_note-7">[7]</a></sup></li>
</ol></div></td></tr></tbody></table>
<p><b>Poland</b> is a country in <a href="/wiki/Central_Europe" title="Central Europe">Central Europe</a>.<sup id="cite_ref-unee_8-0" class="reference"><a href="#cite_note-unee-8">[8]</a></sup> Its official name is <b>Republic of Poland</b>. It is on the east of <a href="/wiki/Germany" title="Germany">Germany</a> (along <a href="/wiki/Oder" class="mw-redirect" title="Oder">Oder</a> and <a href="/wiki/Lusatian_Neisse" title="Lusatian Neisse">Lusatian Neisse</a>). The <a href="/wiki/Czech_Republic" title="Czech Republic">Czech Republic</a> and <a href="/wiki/Slovakia" title="Slovakia">Slovakia</a> are to the south, <a href="/wiki/Ukraine" title="Ukraine">Ukraine</a> and <a href="/wiki/Belarus" title="Belarus">Belarus</a> to the east, and the <a href="/wiki/Baltic_Sea" title="Baltic Sea">Baltic Sea</a>, <a href="/wiki/Lithuania" title="Lithuania">Lithuania</a>, and the <a href="/wiki/Russia" title="Russia">Russian</a> <a href="/wiki/Exclave" title="Exclave">exclave</a> <a href="/wiki/Kaliningrad" title="Kaliningrad">Kaliningrad</a> to the north. The total land area of Poland is about 312,679&nbsp;km<sup>2</sup><sup id="cite_ref-CIAWFBook_9-0" class="reference"><a href="#cite_note-CIAWFBook-9">[9]</a></sup> (120,728&nbsp;mi<sup>2</sup>), slightly larger than Oman. This makes Poland the 77th largest country<sup id="cite_ref-CIAWFBook_9-1" class="reference"><a href="#cite_note-CIAWFBook-9">[9]</a></sup> in the world with over 38.5 million people. Most Polish people live in large cities, including the capital, <a href="/wiki/Warsaw" title="Warsaw">Warsaw</a> (<a href="/wiki/Polish_language" title="Polish language">Polish</a>: <i>Warszawa</i>), <a href="/wiki/%C5%81%C3%B3d%C5%BA" title="Łódź">Łódź</a>, <a href="/wiki/Krak%C3%B3w" title="Kraków">Cracow</a> (<a href="/wiki/Polish_language" title="Polish language">Polish</a>: <i>Kraków</i>), the second capital of Poland (first was <a href="/wiki/Gniezno" title="Gniezno">Gniezno</a>), <a href="/wiki/Szczecin" title="Szczecin">Szczecin</a>, <a href="/wiki/Gda%C5%84sk" title="Gdańsk">Gdańsk</a>, <a href="/wiki/Wroc%C5%82aw" title="Wrocław">Wrocław</a> and <a href="/wiki/Pozna%C5%84" title="Poznań">Poznań</a>.
</p><p>The word "Poland" was written officially for the first time in 966. In 1569, Poland formed a strong union with Lithuania called the <a href="/wiki/Polish-Lithuanian_Commonwealth" class="mw-redirect" title="Polish-Lithuanian Commonwealth">Polish-Lithuanian Commonwealth</a>. At some point in its history, it was the largest <a href="/wiki/State" title="State">state</a> in Europe and became very influential. Much of the territory that now makes up Central European states used to belong to that Commonwealth. Eventually, after a slow decline, the Commonwealth <a href="/wiki/Partitions_of_Poland" title="Partitions of Poland">collapsed</a> in 1795. Poland regained its <a href="/wiki/Independence" title="Independence">independence</a> in 1918 after <a href="/wiki/World_War_I" title="World War I">World War I</a>. In 1921, Poland defeated Soviet Russia in the <a href="/wiki/Polish-Soviet_War" class="mw-redirect" title="Polish-Soviet War">Polish-Soviet War</a> that started in <a href="/wiki/1919" title="1919">1919</a>.
</p><p>However, Poland lost independence again not long after the beginning of <a href="/wiki/World_War_II" title="World War II">World War II</a>, after suffering a defeat by both the <a href="/wiki/USSR" class="mw-redirect" title="USSR">USSR</a> and <a href="/wiki/Nazi_Germany" title="Nazi Germany">Nazi Germany</a>. Although the government collapsed, the Polish people fought on by forming the largest and most effective resistance movement in Nazi-occupied Europe. It is most notable for disrupting German supply lines to the Eastern Front of WWII, providing military intelligence to the <a href="/wiki/United_Kingdom" title="United Kingdom">British</a>, and for saving more <a href="/wiki/Jews" class="mw-redirect" title="Jews">Jewish</a> lives in the <a href="/wiki/Holocaust" class="mw-redirect" title="Holocaust">Holocaust</a> than any other <a href="/wiki/Allies_of_World_War_II" title="Allies of World War II">Allied</a> organization or government. After the war, Poland regained "independence" and became a <a href="/wiki/People%27s_Republic_of_Poland" class="mw-redirect" title="People's Republic of Poland">communist country</a> within the <a href="/wiki/Eastern_Bloc" title="Eastern Bloc">Eastern Bloc</a>. The new government was appointed by <a href="/wiki/Joseph_Stalin" title="Joseph Stalin">Joseph Stalin</a> and was under the control of the <a href="/wiki/Soviet_Union" title="Soviet Union">Soviet Union</a>.
</p><p>In 1989, Poland ceased being a communist country and became a <a href="/wiki/Liberal_democracy" class="mw-redirect" title="Liberal democracy">liberal democracy</a>. Its change of government was the first in a series of events that led to the states of Eastern and Central Europe regaining their <a href="/wiki/Independence" title="Independence">independence</a> and the fall of the USSR in 1991. After the <a href="/wiki/Democratic_consolidation" class="mw-redirect" title="Democratic consolidation">democratic consolidation</a>, Poland joined the <a href="/wiki/European_Union" title="European Union">European Union</a> on 1 May 2004. Poland is also a member of <a href="/wiki/NATO" title="NATO">NATO</a>, the <a href="/wiki/United_Nations" title="United Nations">United Nations</a>, and the <a href="/wiki/World_Trade_Organization" title="World Trade Organization">World Trade Organization</a>.
</p>
<div id="toc" class="toc" role="navigation" aria-labelledby="mw-toc-heading"><input type="checkbox" role="button" id="toctogglecheckbox" class="toctogglecheckbox" style="display:none"><div class="toctitle" lang="en" dir="ltr"><h2 id="mw-toc-heading">Contents</h2><span class="toctogglespan"><label class="toctogglelabel" for="toctogglecheckbox"></label></span></div>
<ul>
<li class="toclevel-1 tocsection-1"><a href="#History"><span class="tocnumber">1</span> <span class="toctext">History</span></a>
<ul>
<li class="toclevel-2 tocsection-2"><a href="#Early_history"><span class="tocnumber">1.1</span> <span class="toctext">Early history</span></a></li>
<li class="toclevel-2 tocsection-3"><a href="#Piast_and_Jagiellon_dynasties"><span class="tocnumber">1.2</span> <span class="toctext">Piast and Jagiellon dynasties</span></a></li>
<li class="toclevel-2 tocsection-4"><a href="#Polish-Lithuanian_Commonwealth_to_Second_Republic_of_Poland"><span class="tocnumber">1.3</span> <span class="toctext">Polish-Lithuanian Commonwealth to Second Republic of Poland</span></a></li>
<li class="toclevel-2 tocsection-5"><a href="#World_War_II"><span class="tocnumber">1.4</span> <span class="toctext">World War II</span></a></li>
<li class="toclevel-2 tocsection-6"><a href="#Polish_People's_Republic_to_Third_Polish_Republic"><span class="tocnumber">1.5</span> <span class="toctext">Polish People's Republic to Third Polish Republic</span></a></li>
</ul>
</li>
<li class="toclevel-1 tocsection-7"><a href="#Geography"><span class="tocnumber">2</span> <span class="toctext">Geography</span></a>
<ul>
<li class="toclevel-2 tocsection-8"><a href="#Administrative_divisions"><span class="tocnumber">2.1</span> <span class="toctext">Administrative divisions</span></a></li>
</ul>
</li>
<li class="toclevel-1 tocsection-9"><a href="#Literature"><span class="tocnumber">3</span> <span class="toctext">Literature</span></a></li>
<li class="toclevel-1 tocsection-10"><a href="#People"><span class="tocnumber">4</span> <span class="toctext">People</span></a></li>
<li class="toclevel-1 tocsection-11"><a href="#Famous_people"><span class="tocnumber">5</span> <span class="toctext">Famous people</span></a></li>
<li class="toclevel-1 tocsection-12"><a href="#Urban_demographics"><span class="tocnumber">6</span> <span class="toctext">Urban demographics</span></a></li>
<li class="toclevel-1 tocsection-13"><a href="#Related_pages"><span class="tocnumber">7</span> <span class="toctext">Related pages</span></a></li>
<li class="toclevel-1 tocsection-14"><a href="#References"><span class="tocnumber">8</span> <span class="toctext">References</span></a></li>
<li class="toclevel-1 tocsection-15"><a href="#Other_websites"><span class="tocnumber">9</span> <span class="toctext">Other websites</span></a></li>
</ul>
</div>

<h2><span class="mw-headline" id="History">History</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Poland&amp;veaction=edit&amp;section=1" class="mw-editsection-visualeditor" title="Change section: History">change</a><span class="mw-editsection-divider"> | </span><a href="/w/index.php?title=Poland&amp;action=edit&amp;section=1" title="Change section: History">change source</a><span class="mw-editsection-bracket">]</span></span></h2>
<style data-mw-deduplicate="TemplateStyles:r7707418">.mw-parser-output .hatnote{font-style:italic}.mw-parser-output div.hatnote{padding-left:1.6em;margin-bottom:0.5em}.mw-parser-output .hatnote i{font-style:normal}.mw-parser-output .hatnote+link+.hatnote{margin-top:-0.5em}</style><div role="note" class="hatnote navigation-not-searchable">Main article: <a href="/wiki/History_of_Poland" title="History of Poland">History of Poland</a></div>
<h3><span class="mw-headline" id="Early_history">Early history</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Poland&amp;veaction=edit&amp;section=2" class="mw-editsection-visualeditor" title="Change section: Early history">change</a><span class="mw-editsection-divider"> | </span><a href="/w/index.php?title=Poland&amp;action=edit&amp;section=2" title="Change section: Early history">change source</a><span class="mw-editsection-bracket">]</span></span></h3>
<div class="thumb tleft"><div class="thumbinner" style="width:222px;"><a href="/wiki/File:Slavic_tribes_in_the_7th_to_9th_century.jpg" class="image"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Slavic_tribes_in_the_7th_to_9th_century.jpg/220px-Slavic_tribes_in_the_7th_to_9th_century.jpg" decoding="async" width="220" height="209" class="thumbimage" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Slavic_tribes_in_the_7th_to_9th_century.jpg/330px-Slavic_tribes_in_the_7th_to_9th_century.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Slavic_tribes_in_the_7th_to_9th_century.jpg/440px-Slavic_tribes_in_the_7th_to_9th_century.jpg 2x" data-file-width="1520" data-file-height="1442"></a>  <div class="thumbcaption"><div class="magnify"><a href="/wiki/File:Slavic_tribes_in_the_7th_to_9th_century.jpg" class="internal" title="Enlarge"></a></div>Slavic tribes 600-800</div></div></div>
<p>The first sign of humans in Polish lands was 500,000 years ago. The <a href="/wiki/Bronze_Age" title="Bronze Age">Bronze Age</a> started around 2400-2300 <a href="/wiki/BC" class="mw-redirect" title="BC">BC</a>. The <a href="/wiki/Iron_Age" title="Iron Age">Iron Age</a> started around 750-700 <a href="/wiki/BC" class="mw-redirect" title="BC">BC</a>. At that time the Polish lands were under the influence of the <a href="/w/index.php?title=Lusatian_culture&amp;action=edit&amp;redlink=1" class="new" title="Lusatian culture (not yet started)">Lusatian culture</a>. About 400 BC <a href="/wiki/Celts" title="Celts">Celtic</a> and <a href="/wiki/Germanic_people" class="mw-redirect" title="Germanic people">Germanic</a> tribes lived there. Those people had trade contacts with the <a href="/wiki/Roman_Empire" title="Roman Empire">Roman Empire</a>.
</p><p>Over time, <a href="/wiki/Slavs" title="Slavs">Slavs</a> came to Polish lands. Some of those Slavs, now commonly referred to as Western Slavs (though in reality a diverse group of tribes with shared ethnic and cultural features), stayed there and started to create new nations. The most powerful tribe was called the <a href="/wiki/Polans" title="Polans">Polans</a>, who united all of the other Slavic tribes living there, and this is where the name "Poland" comes from.
</p>
<h3><span class="mw-headline" id="Piast_and_Jagiellon_dynasties">Piast and Jagiellon dynasties</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Poland&amp;veaction=edit&amp;section=3" class="mw-editsection-visualeditor" title="Change section: Piast and Jagiellon dynasties">change</a><span class="mw-editsection-divider"> | </span><a href="/w/index.php?title=Poland&amp;action=edit&amp;section=3" title="Change section: Piast and Jagiellon dynasties">change source</a><span class="mw-editsection-bracket">]</span></span></h3>
<div class="thumb tleft"><div class="thumbinner" style="width:222px;"><a href="/wiki/File:Polska_960_-_992.svg" class="image"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/3/32/Polska_960_-_992.svg/220px-Polska_960_-_992.svg.png" decoding="async" width="220" height="217" class="thumbimage" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/3/32/Polska_960_-_992.svg/330px-Polska_960_-_992.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/3/32/Polska_960_-_992.svg/440px-Polska_960_-_992.svg.png 2x" data-file-width="11510" data-file-height="11360"></a>  <div class="thumbcaption"><div class="magnify"><a href="/wiki/File:Polska_960_-_992.svg" class="internal" title="Enlarge"></a></div>Poland 960-992</div></div></div>
<div class="thumb tright"><div class="thumbinner" style="width:222px;"><a href="/wiki/File:Boleslaus_I.jpg" class="image"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Boleslaus_I.jpg/220px-Boleslaus_I.jpg" decoding="async" width="220" height="285" class="thumbimage" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Boleslaus_I.jpg/330px-Boleslaus_I.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Boleslaus_I.jpg/440px-Boleslaus_I.jpg 2x" data-file-width="463" data-file-height="600"></a>  <div class="thumbcaption"><div class="magnify"><a href="/wiki/File:Boleslaus_I.jpg" class="internal" title="Enlarge"></a></div><a href="/wiki/Boleslaw_I_of_Poland" title="Boleslaw I of Poland">Boleslaw I of Poland</a></div></div></div>
<p>Poland began to form a country around the middle of the <a href="/wiki/10th_century" title="10th century">10th century</a> in the <a href="/wiki/Piast_dynasty" title="Piast dynasty">Piast dynasty</a>. In 966, Prince <a href="/wiki/Mieszko_I" class="mw-redirect" title="Mieszko I">Mieszko I</a> became a <a href="/wiki/Christian" title="Christian">Christian</a>, and so the Polish people also became Christians. The next king was <a href="/w/index.php?title=Boles%C5%82aw_I_of_Poland&amp;action=edit&amp;redlink=1" class="new" title="Bolesław I of Poland (not yet started)">Bolesław I of Poland</a> (called Bolesław the Brave). He conquered many lands and he became the first King of Poland. <a href="/w/index.php?title=Casimir_I_of_Poland&amp;action=edit&amp;redlink=1" class="new" title="Casimir I of Poland (not yet started)">Casimir I of Poland</a> changed the Polish capital from <a href="/wiki/Gniezno" title="Gniezno">Gniezno</a> to <a href="/wiki/Krak%C3%B3w" title="Kraków">Kraków</a>. In the 12th century, Poland broke into some smaller <a href="/wiki/States" class="mw-redirect" title="States">states</a> after the death of King <a href="/w/index.php?title=Boles%C5%82aw_III_Wrymouth&amp;action=edit&amp;redlink=1" class="new" title="Bolesław III Wrymouth (not yet started)">Bolesław III Wrymouth</a> in 1138 because of his <a href="/wiki/Will_(law)" title="Will (law)">will</a>. Those states were later attacked by <a href="/wiki/Mongol" class="mw-redirect" title="Mongol">Mongol</a> armies in 1241, which slowed down the unification of the small states into the big country of Poland. This happened eighty years later, in 1320 when <a href="/w/index.php?title=W%C5%82adys%C5%82aw_I_of_Poland&amp;action=edit&amp;redlink=1" class="new" title="Władysław I of Poland (not yet started)">Władysław I</a> became the King of United Poland. His son <a href="/wiki/Casimir_III" class="mw-redirect" title="Casimir III">Casimir III</a> the Great reformed the Polish economy, built new castles, and won the war against the <a href="/w/index.php?title=Ruthenian_Dukedom&amp;action=edit&amp;redlink=1" class="new" title="Ruthenian Dukedom (not yet started)">Ruthenian Dukedom</a>. Many people <a href="/wiki/Emigration" title="Emigration">emigrated</a> to Poland, becoming a haven for emigrants. Many <a href="/wiki/Jewish" class="mw-redirect" title="Jewish">Jewish</a> people also moved into Poland during that time. The <a href="/wiki/Black_Death" title="Black Death">Black Death</a>, which affected many parts of <a href="/wiki/Europe" title="Europe">Europe</a> from 1347 to 1351, did not come to Poland.<sup id="cite_ref-REF03_10-0" class="reference"><a href="#cite_note-REF03-10">[10]</a></sup>
</p><p>After the death of the last Piast on the Polish throne, <a href="/wiki/Casimir_III_of_Poland" title="Casimir III of Poland">Casimir III</a>, <a href="/w/index.php?title=Louis_I_of_Hungary&amp;action=edit&amp;redlink=1" class="new" title="Louis I of Hungary (not yet started)">Louis I of Hungary</a> and his daughter <a href="/wiki/Jadwiga_of_Poland" title="Jadwiga of Poland">Jadwiga of Poland</a> began their rule. She married the <a href="/wiki/Lithuania" title="Lithuania">Lithuanian</a> prince <a href="/w/index.php?title=Jogaila&amp;action=edit&amp;redlink=1" class="new" title="Jogaila (not yet started)">Jogaila</a>. Their marriage started a new dynasty in Poland: the <a href="/wiki/Jagiellon_dynasty" title="Jagiellon dynasty">Jagiellon dynasty</a>. Under the <a href="/wiki/Jagiellon_dynasty" title="Jagiellon dynasty">Jagiellon dynasty</a>, Poland made an alliance with its neighbor <a href="/wiki/Lithuania" title="Lithuania">Lithuania</a>.
</p>
<h3><span class="mw-headline" id="Polish-Lithuanian_Commonwealth_to_Second_Republic_of_Poland">Polish-Lithuanian Commonwealth to Second Republic of Poland</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Poland&amp;veaction=edit&amp;section=4" class="mw-editsection-visualeditor" title="Change section: Polish-Lithuanian Commonwealth to Second Republic of Poland">change</a><span class="mw-editsection-divider"> | </span><a href="/w/index.php?title=Poland&amp;action=edit&amp;section=4" title="Change section: Polish-Lithuanian Commonwealth to Second Republic of Poland">change source</a><span class="mw-editsection-bracket">]</span></span></h3>
<div class="thumb tleft"><div class="thumbinner" style="width:222px;"><a href="/wiki/File:Irp1635.jpg" class="image"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/21/Irp1635.jpg/220px-Irp1635.jpg" decoding="async" width="220" height="172" class="thumbimage" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/21/Irp1635.jpg/330px-Irp1635.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/21/Irp1635.jpg/440px-Irp1635.jpg 2x" data-file-width="2000" data-file-height="1568"></a>  <div class="thumbcaption"><div class="magnify"><a href="/wiki/File:Irp1635.jpg" class="internal" title="Enlarge"></a></div>Polish-Lithuanian Union when it was largest 1618-1655</div></div></div>
<p>In the 17th century <a href="/wiki/Sweden" title="Sweden">Sweden</a> attacked almost all of Poland (this was called “the Deluge”). Many wars against the <a href="/wiki/Ottoman_Empire" title="Ottoman Empire">Ottoman Empire</a>, <a href="/wiki/Russia" title="Russia">Russia</a>, <a href="/wiki/Cossacks" title="Cossacks">Cossacks</a>, <a href="/wiki/Transylvania" title="Transylvania">Transylvania</a> and <a href="/wiki/Brandenburg" title="Brandenburg">Brandenburg</a>-<a href="/wiki/Prussia" title="Prussia">Prussia</a> ended in 1699. For the next 80 years, the government and the nation were weak, making Poland dependent on Russia. Russian <a href="/wiki/Tsars" class="mw-redirect" title="Tsars">tsars</a> took advantage of this by offering money to dishonest members of the Polish <a href="/wiki/Government" title="Government">government</a>, who would block new ideas and solutions. <a href="/wiki/Russia" title="Russia">Russia</a>, <a href="/wiki/Prussia" title="Prussia">Prussia</a>, and <a href="/wiki/Austria" title="Austria">Austria</a> broke Poland into three pieces in 1772, 1793 and 1795, which dissolved the country. Before the second split, a <a href="/wiki/Constitution" title="Constitution">Constitution</a> called "<a href="/w/index.php?title=The_Constitution_of_3_May&amp;action=edit&amp;redlink=1" class="new" title="The Constitution of 3 May (not yet started)">The Constitution of 3 May</a>" was made in 1791. The Polish people did not like the new kings, and often rebelled (two big <a href="/wiki/Rebellion" title="Rebellion">rebellions</a> in 1830<sup id="cite_ref-REF03_10-1" class="reference"><a href="#cite_note-REF03-10">[10]</a></sup> and 1863<sup id="cite_ref-11" class="reference"><a href="#cite_note-11">[11]</a></sup>).
</p><p><a href="/wiki/Napoleon" title="Napoleon">Napoleon</a> made another Polish state, “the <a href="/wiki/Duchy_of_Warsaw" title="Duchy of Warsaw">Duchy of Warsaw</a>”, but after the <a href="/wiki/Napoleonic_wars" class="mw-redirect" title="Napoleonic wars">Napoleonic wars</a>, Poland was split again by the countries at the <a href="/wiki/Congress_of_Vienna" title="Congress of Vienna">Congress of Vienna</a>. The eastern part was ruled by the Russian tsar. During <a href="/wiki/World_War_I" title="World War I">World War I</a> all the <a href="/wiki/Allies_of_World_War_I" class="mw-redirect" title="Allies of World War I">Allies</a> agreed to save Poland. Soon after the <a href="/wiki/Armistice_with_Germany_(Compi%C3%A8gne)" title="Armistice with Germany (Compiègne)">surrender of Germany</a> in November 1918, Poland became the <a href="/wiki/Second_Polish_Republic" title="Second Polish Republic">Second Polish Republic</a> (<i>II Rzeczpospolita Polska</i>). It got its freedom after several military conflicts; the largest was in 1919-1921 <a href="/wiki/Polish-Soviet_War" class="mw-redirect" title="Polish-Soviet War">Polish-Soviet War</a>.
</p>
<h3><span class="mw-headline" id="World_War_II">World War II</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Poland&amp;veaction=edit&amp;section=5" class="mw-editsection-visualeditor" title="Change section: World War II">change</a><span class="mw-editsection-divider"> | </span><a href="/w/index.php?title=Poland&amp;action=edit&amp;section=5" title="Change section: World War II">change source</a><span class="mw-editsection-bracket">]</span></span></h3>
<div class="thumb tleft"><div class="thumbinner" style="width:222px;"><a href="/wiki/File:RzeczpospolitaII.png" class="image"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/3/3b/RzeczpospolitaII.png/220px-RzeczpospolitaII.png" decoding="async" width="220" height="211" class="thumbimage" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/3/3b/RzeczpospolitaII.png/330px-RzeczpospolitaII.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/3/3b/RzeczpospolitaII.png/440px-RzeczpospolitaII.png 2x" data-file-width="1112" data-file-height="1069"></a>  <div class="thumbcaption"><div class="magnify"><a href="/wiki/File:RzeczpospolitaII.png" class="internal" title="Enlarge"></a></div>Poland 1922-1939</div></div></div>
<p>On September 1, 1939, <a href="/wiki/World_War_II" title="World War II">World War II</a> started when <a href="/wiki/Nazi_Germany" title="Nazi Germany">Nazi Germany</a> <a href="/wiki/Invasion_of_Poland_(1939)" title="Invasion of Poland (1939)">attacked Poland</a>. The <a href="/wiki/Soviet_Union" title="Soviet Union">Soviet Union</a> attacked Poland on September 17, 1939. <a href="/wiki/Warsaw" title="Warsaw">Warsaw</a> was defeated on September 28, 1939. Poland was split into two pieces, one half owned by Nazi Germany, the other by the Soviet Union. More than 6 million Polish people died, and half of these people were <a href="/wiki/Jews" class="mw-redirect" title="Jews">Jewish</a>. Most of these deaths were part of the <a href="/wiki/Holocaust" class="mw-redirect" title="Holocaust">Holocaust</a>, in which 6 million Jews were killed. At the war's end, Poland's borders were moved west, pushing the eastern border to the <a href="/w/index.php?title=Curzon_line&amp;action=edit&amp;redlink=1" class="new" title="Curzon line (not yet started)">Curzon line</a>.<sup id="cite_ref-12" class="reference"><a href="#cite_note-12">[12]</a></sup> The western border was moved to the <a href="/wiki/Oder-Neisse_line" title="Oder-Neisse line">Oder-Neisse line</a>. The new Poland became 20% smaller by 77,500 square kilometers (29,900 sq mi). The shift forced millions of Poles, Germans, Ukrainians, and Jews to move.
</p>
<div style="clear:left;"></div>
<h3><span id="Polish_People.27s_Republic_to_Third_Polish_Republic"></span><span class="mw-headline" id="Polish_People's_Republic_to_Third_Polish_Republic">Polish People's Republic to Third Polish Republic</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Poland&amp;veaction=edit&amp;section=6" class="mw-editsection-visualeditor" title="Change section: Polish People's Republic to Third Polish Republic">change</a><span class="mw-editsection-divider"> | </span><a href="/w/index.php?title=Poland&amp;action=edit&amp;section=6" title="Change section: Polish People's Republic to Third Polish Republic">change source</a><span class="mw-editsection-bracket">]</span></span></h3>
<div class="thumb tright"><div class="thumbinner" style="width:222px;"><a href="/wiki/File:Curzon_line_en.svg" class="image"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Curzon_line_en.svg/220px-Curzon_line_en.svg.png" decoding="async" width="220" height="200" class="thumbimage" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Curzon_line_en.svg/330px-Curzon_line_en.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Curzon_line_en.svg/440px-Curzon_line_en.svg.png 2x" data-file-width="563" data-file-height="513"></a>  <div class="thumbcaption"><div class="magnify"><a href="/wiki/File:Curzon_line_en.svg" class="internal" title="Enlarge"></a></div>Poland's current boundaries were made after 1945. The grey areas went from Poland to the Soviet Union. The red areas from Germany to Poland.</div></div></div>
<p>After these events, Poland gradually became a <a href="/wiki/Communism" title="Communism">communist</a> country. It was supposedly an independent country. But in reality, the new government was appointed by <a href="/wiki/Joseph_Stalin" title="Joseph Stalin">Joseph Stalin</a>. It was also under the control of the <a href="/wiki/Soviet_Union" title="Soviet Union">Soviet Union</a>. The country was then renamed the <a href="/wiki/People%27s_Republic_of_Poland" class="mw-redirect" title="People's Republic of Poland">People's Republic of Poland</a>. There are many Poles in the neighboring countries <a href="/wiki/Ukraine" title="Ukraine">Ukraine</a>, <a href="/wiki/Belarus" title="Belarus">Belarus</a>, and Lithuania (these three countries were part of the Soviet Union until 1991), as well as in other countries. Most Poles outside of Poland are in the United States, especially in <a href="/wiki/Chicago" title="Chicago">Chicago</a>. Germany and the <a href="/wiki/United_Kingdom" title="United Kingdom">United Kingdom</a> are also home to a large Polish diaspora. The most recent mass emigration of Poles to western countries began after 1989.
</p><p>In 1989 <a href="/wiki/Solidarity" class="mw-disambig" title="Solidarity">Solidarity</a> - a <a href="/wiki/Trade_union" class="mw-redirect" title="Trade union">trade union</a> led by <a href="/wiki/Lech_Wa%C5%82%C4%99sa" title="Lech Wałęsa">Lech Wałęsa</a> - helped defeat the communist government in Poland. Even before that event, Lech Wałęsa was given a <a href="/wiki/Nobel_Prize" title="Nobel Prize">Nobel Prize</a> for leading the first non-communist trade union fighting for democracy in the <a href="/wiki/Eastern_Bloc" title="Eastern Bloc">Communist Block</a>. When Communism ended in Poland there were many improvements in human rights, such as <a href="/wiki/Freedom_of_speech" title="Freedom of speech">freedom of speech</a>, <a href="/wiki/Democracy" title="Democracy">democracy</a>, etc. In 1991 Poland became a member of the <a href="/wiki/Visegrad_Group" class="mw-redirect" title="Visegrad Group">Visegrad Group</a> and joined <a href="/wiki/NATO" title="NATO">NATO</a> in 1999 along with the <a href="/wiki/Czech_Republic" title="Czech Republic">Czech Republic</a> and <a href="/wiki/Hungary" title="Hungary">Hungary</a>. Polish voters then voted to join the <a href="/wiki/European_Union" title="European Union">European Union</a> in a vote in June 2003. The country joined the <a href="/wiki/EU" class="mw-redirect" title="EU">EU</a> on May 1, 2004.
</p><p>Currently, the Prime Minister is <a href="/wiki/Mateusz_Morawiecki" title="Mateusz Morawiecki">Mateusz Morawiecki</a>. On 10 April 2010 the President <a href="/wiki/Lech_Kaczy%C5%84ski" title="Lech Kaczyński">Lech Kaczyński</a> died in a government plane crash in <a href="/wiki/Smolensk" title="Smolensk">Smolensk</a> in <a href="/wiki/Russia" title="Russia">Russia</a>. The president is elected directly by the citizens for a five-year <a href="/wiki/Term" class="mw-redirect" title="Term">term</a>. The Prime Minister is appointed by the President and confirmed by the "Sejm". The Sejm is the lower chamber of Parliament <a href="/wiki/Legislature" title="Legislature">legislature</a> for the country. It has 460 deputies <a href="/wiki/Elect" class="mw-redirect" title="Elect">elected</a> every four years.
</p>
<h2><span class="mw-headline" id="Geography">Geography</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Poland&amp;veaction=edit&amp;section=7" class="mw-editsection-visualeditor" title="Change section: Geography">change</a><span class="mw-editsection-divider"> | </span><a href="/w/index.php?title=Poland&amp;action=edit&amp;section=7" title="Change section: Geography">change source</a><span class="mw-editsection-bracket">]</span></span></h2>
<div class="thumb tright"><div class="thumbinner" style="width:222px;"><a href="/wiki/File:Poland_topo.jpg" class="image"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Poland_topo.jpg/220px-Poland_topo.jpg" decoding="async" width="220" height="214" class="thumbimage" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Poland_topo.jpg/330px-Poland_topo.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Poland_topo.jpg/440px-Poland_topo.jpg 2x" data-file-width="1400" data-file-height="1364"></a>  <div class="thumbcaption"><div class="magnify"><a href="/wiki/File:Poland_topo.jpg" class="internal" title="Enlarge"></a></div>Physical land features of Poland</div></div></div>
<p>Poland's territory is a <a href="/wiki/Plain" title="Plain">plain</a> reaching from the <a href="/wiki/Baltic_Sea" title="Baltic Sea">Baltic Sea</a> in the north to the <a href="/wiki/Carpathian_Mountains" title="Carpathian Mountains">Carpathian Mountains</a> in the south. Within that plain, the land varies from east to west.
</p><p>The Polish Baltic coast is mostly smooth but has natural <a href="/wiki/Harbor" title="Harbor">harbors</a> in the <a href="/wiki/Tricity" title="Tricity">Gdańsk-Gdynia</a> region and <a href="/wiki/Szczecin" title="Szczecin">Szczecin</a> in the far northwest. This coast has several <a href="/wiki/Spit" title="Spit">spits</a>, <a href="/wiki/Dune" title="Dune">dunes</a>, and coastal lakes. Coast lakes are former <a href="/wiki/Bay" class="mw-redirect" title="Bay">bays</a> that have been cut off from the sea. These areas are sometimes called lagoons. <a href="/wiki/Szczecin_Lagoon" title="Szczecin Lagoon">Szczecin Lagoon</a> is on the western border with <a href="/wiki/Germany" title="Germany">Germany</a>. The <a href="/w/index.php?title=Vistula_Lagoon&amp;action=edit&amp;redlink=1" class="new" title="Vistula Lagoon (not yet started)">Vistula Lagoon</a> is on the eastern border with <a href="/wiki/Kaliningrad" title="Kaliningrad">Kaliningrad</a>, province of <a href="/wiki/Russia" title="Russia">Russia</a>. The longest river in Poland, the <a href="/wiki/Vistula" title="Vistula">Vistula</a> river, empties into the <a href="/w/index.php?title=Vistula_Lagoon&amp;action=edit&amp;redlink=1" class="new" title="Vistula Lagoon (not yet started)">Vistula Lagoon</a> and also directly into the <a href="/wiki/Baltic_Sea" title="Baltic Sea">Baltic Sea</a>.
</p><p>The northeastern region is densely wooded, sparsely populated, and lacks agricultural and industrial resources. The geographical region has four hilly <a href="/wiki/District" title="District">districts</a> of <a href="/wiki/Moraine" title="Moraine">moraines</a> and lakes created by moraines. These formed during and after the <a href="/wiki/Pleistocene" title="Pleistocene">Pleistocene</a> <a href="/wiki/Ice_age" title="Ice age">ice age</a>. The Masurian Lake District is the largest of the four districts and covers much of northeastern Poland.
</p><p>Poland has many lakes. In Europe, only <a href="/wiki/Finland" title="Finland">Finland</a> has more lakes. The largest lakes are <a href="/w/index.php?title=%C5%9Aniardwy&amp;action=edit&amp;redlink=1" class="new" title="Śniardwy (not yet started)">Śniardwy</a> and <a href="/w/index.php?title=Lake_Mamry&amp;action=edit&amp;redlink=1" class="new" title="Lake Mamry (not yet started)">Mamry</a>. In addition to the lake districts in the north, there are also many mountain lakes in the <a href="/w/index.php?title=Tatras_Mountains&amp;action=edit&amp;redlink=1" class="new" title="Tatras Mountains (not yet started)">Tatras mountains</a>.
</p><p>South of the northeastern region is the regions of <a href="/wiki/Silesia" title="Silesia">Silesia</a> and <a href="/w/index.php?title=Masovia&amp;action=edit&amp;redlink=1" class="new" title="Masovia (not yet started)">Masovia</a>, which are marked by the broad ice-age river <a href="/wiki/Valley" title="Valley">valleys</a>. The Silesia region has many resources and people. <a href="/wiki/Coal" title="Coal">Coal</a> is abundant. Lower Silesia has large <a href="/wiki/Copper" title="Copper">copper</a> mining. <a href="/w/index.php?title=Mazovian_Lowland&amp;action=edit&amp;redlink=1" class="new" title="Mazovian Lowland (not yet started)">Masovian Plain</a> is in central Poland. It is in the valleys of three large rivers: <a href="/wiki/Vistula" title="Vistula">Vistula</a>, <a href="/wiki/Bug_River" title="Bug River">Bug</a> and <a href="/wiki/Narew" title="Narew">Narew</a>.
</p><p>Further south is the Polish mountain region. These mountains include the <a href="/wiki/Sudetes" title="Sudetes">Sudetes</a> and the <a href="/wiki/Carpathian_Mountains" title="Carpathian Mountains">Carpathian Mountains</a>. The highest part of the Carpathians is the Tatra mountains which is along Poland’s southern border. The tallest mountain in Poland, <a href="/w/index.php?title=Rysy&amp;action=edit&amp;redlink=1" class="new" title="Rysy (not yet started)">Rysy</a> at 2,503 m (8,210&nbsp;ft), is in the <a href="/w/index.php?title=High_Tatras&amp;action=edit&amp;redlink=1" class="new" title="High Tatras (not yet started)">High Tatras</a>.
</p>
<h3><span class="mw-headline" id="Administrative_divisions">Administrative divisions</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Poland&amp;veaction=edit&amp;section=8" class="mw-editsection-visualeditor" title="Change section: Administrative divisions">change</a><span class="mw-editsection-divider"> | </span><a href="/w/index.php?title=Poland&amp;action=edit&amp;section=8" title="Change section: Administrative divisions">change source</a><span class="mw-editsection-bracket">]</span></span></h3>
<p>Poland is made of sixteen <a href="/wiki/Region" title="Region">regions</a> known as <a href="/wiki/Voivodeship" title="Voivodeship">voivodeships</a> (<i>województwa</i>, singular - <i>województwo</i>). They are basically created from the country's historical regions, whereas those of the past two decades (till 1998) had been focused on and named for separate cities. The new units range in areas from under 10,000&nbsp;km<sup>2</sup> (Opole Voivodeship) to over 35,000&nbsp;km<sup>2</sup> (Masovian Voivodeship). Voivodeships are controlled by voivod governments, and their legislatures are called <a href="/w/index.php?title=Voivodeship_sejmik&amp;action=edit&amp;redlink=1" class="new" title="Voivodeship sejmik (not yet started)">voivodeship sejmiks</a>.
</p><p>The sixteen voivodeships that make up Poland are further divided into <i><a href="/wiki/Powiat" title="Powiat">powiaty</a></i> (singular <i>powiat</i>), second-level units of <a href="/wiki/Local_government" title="Local government">administration</a>, which are about the same as to a <a href="/wiki/County" title="County">county</a>, <a href="/wiki/District" title="District">district</a> or <a href="/wiki/Prefecture" title="Prefecture">prefecture</a> in other countries.
</p>
<table>
<tbody><tr>
<td valign="top">
<table style="width:420px; background:transparent;">
<tbody><tr>
<td>
<table class="wikitable" style="width:100%; font-size:95%;">
<tbody><tr>
<th colspan="2"><a href="/wiki/Voivodeship" title="Voivodeship">Voivodeship</a></th>
<th rowspan="2">Capital city or cities
</th></tr>
<tr>
<th width="26%"></th>
<th width="29%"><i><a href="/wiki/Polish_language" title="Polish language">in Polish</a></i>
</th></tr>
<tr>
<td><a href="/wiki/Kuyavian-Pomeranian_Voivodeship" title="Kuyavian-Pomeranian Voivodeship">Kuyavia-Pomerania</a></td>
<td><i>Kujawsko-Pomorskie</i>
</td>
<td style="font-size:90%;"><a href="/wiki/Bydgoszcz" title="Bydgoszcz">Bydgoszcz</a>&nbsp;/ <a href="/wiki/Toru%C5%84" title="Toruń">Toruń</a>
</td></tr>
<tr>
<td><a href="/wiki/Greater_Poland_Voivodeship" title="Greater Poland Voivodeship">Greater Poland</a></td>
<td><i>Wielkopolskie</i></td>
<td style="font-size:90%;"><a href="/wiki/Pozna%C5%84" title="Poznań">Poznań</a>
</td></tr>
<tr>
<td><a href="/wiki/Lesser_Poland_Voivodeship" title="Lesser Poland Voivodeship">Lesser Poland</a></td>
<td><i>Małopolskie</i></td>
<td style="font-size:90%;"><a href="/wiki/Krak%C3%B3w" title="Kraków">Kraków</a>
</td></tr>
<tr>
<td><a href="/wiki/%C5%81%C3%B3d%C5%BA_Voivodeship" title="Łódź Voivodeship">Łódź</a></td>
<td><i>Łódzkie</i></td>
<td style="font-size:90%;"><a href="/wiki/%C5%81%C3%B3d%C5%BA" title="Łódź">Łódź</a>
</td></tr>
<tr>
<td><a href="/wiki/Lower_Silesian_Voivodeship" title="Lower Silesian Voivodeship">Lower Silesia</a></td>
<td><i>Dolnośląskie</i></td>
<td style="font-size:90%;"><a href="/wiki/Wroc%C5%82aw" title="Wrocław">Wrocław</a>
</td></tr>
<tr>
<td><a href="/wiki/Lublin_Voivodeship" title="Lublin Voivodeship">Lublin</a></td>
<td><i>Lubelskie</i></td>
<td style="font-size:90%;"><a href="/wiki/Lublin" title="Lublin">Lublin</a>
</td></tr>
<tr>
<td><a href="/wiki/Lubusz_Voivodeship" title="Lubusz Voivodeship">Lubusz</a></td>
<td><i>Lubuskie</i></td>
<td style="font-size:90%;"><a href="/wiki/Gorz%C3%B3w_Wielkopolski" title="Gorzów Wielkopolski">Gorzów Wielkopolski</a>&nbsp;/ <a href="/wiki/Zielona_G%C3%B3ra" title="Zielona Góra">Zielona Góra</a>
</td></tr>
<tr>
<td><a href="/wiki/Masovian_Voivodeship" title="Masovian Voivodeship">Masovia</a></td>
<td><i>Mazowieckie</i></td>
<td style="font-size:90%;"><a href="/wiki/Warsaw" title="Warsaw">Warsaw</a> (National Capital)
</td></tr>
<tr>
<td><a href="/wiki/Opole_Voivodeship" title="Opole Voivodeship">Opole</a></td>
<td><i>Opolskie</i></td>
<td style="font-size:90%;"><a href="/wiki/Opole" title="Opole">Opole</a>
</td></tr>
<tr>
<td><a href="/wiki/Podlaskie_Voivodeship" title="Podlaskie Voivodeship">Podlaskie</a></td>
<td><i>Podlaskie</i></td>
<td style="font-size:90%;"><a href="/wiki/Bia%C5%82ystok" title="Białystok">Białystok</a>
</td></tr>
<tr>
<td><a href="/wiki/Pomeranian_Voivodeship" title="Pomeranian Voivodeship">Pomerania</a></td>
<td><i>Pomorskie</i></td>
<td style="font-size:90%;"><a href="/wiki/Gda%C5%84sk" title="Gdańsk">Gdańsk</a>
</td></tr>
<tr>
<td><a href="/wiki/Silesian_Voivodeship" title="Silesian Voivodeship">Silesia</a></td>
<td><i>Śląskie</i></td>
<td style="font-size:90%;"><a href="/wiki/Katowice" title="Katowice">Katowice</a>
</td></tr>
<tr>
<td><a href="/wiki/Subcarpathian_Voivodeship" class="mw-redirect" title="Subcarpathian Voivodeship">Subcarpathia</a></td>
<td><i>Podkarpackie</i></td>
<td style="font-size:90%;"><a href="/wiki/Rzesz%C3%B3w" title="Rzeszów">Rzeszów</a>
</td></tr>
<tr>
<td><a href="/wiki/Swietokrzyskie_Voivodeship" class="mw-redirect" title="Swietokrzyskie Voivodeship">Swietokrzyskie</a></td>
<td><i>Świętokrzyskie</i></td>
<td style="font-size:90%;"><a href="/wiki/Kielce" title="Kielce">Kielce</a>
</td></tr>
<tr>
<td><a href="/wiki/Warmian-Masurian_Voivodeship" title="Warmian-Masurian Voivodeship">Warmia-Masuria</a></td>
<td><i>Warmińsko-Mazurskie</i>
</td>
<td style="font-size:90%;"><a href="/wiki/Olsztyn" title="Olsztyn">Olsztyn</a>
</td></tr>
<tr>
<td><a href="/wiki/West_Pomeranian_Voivodeship" title="West Pomeranian Voivodeship">West Pomerania</a></td>
<td><i>Zachodniopomorskie</i>
</td>
<td style="font-size:90%;"><a href="/wiki/Szczecin" title="Szczecin">Szczecin</a>
</td></tr></tbody></table>
</td></tr></tbody></table>
</td>
<td valign="top">
<p><a href="/wiki/File:Wojewodztwa.svg" class="image"><img alt="Wojewodztwa.svg" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Wojewodztwa.svg/550px-Wojewodztwa.svg.png" decoding="async" width="550" height="514" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Wojewodztwa.svg/825px-Wojewodztwa.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Wojewodztwa.svg/1100px-Wojewodztwa.svg.png 2x" data-file-width="2061" data-file-height="1925"></a>
</p>
</td>
<td>
</td></tr></tbody></table>
<h2><span class="mw-headline" id="Literature">Literature</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Poland&amp;veaction=edit&amp;section=9" class="mw-editsection-visualeditor" title="Change section: Literature">change</a><span class="mw-editsection-divider"> | </span><a href="/w/index.php?title=Poland&amp;action=edit&amp;section=9" title="Change section: Literature">change source</a><span class="mw-editsection-bracket">]</span></span></h2>
<div class="thumb tright"><div class="thumbinner" style="width:172px;"><a href="/wiki/File:Henryk_sienkiewicz_by_kazimierz_pochwalski.png" class="image"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/6/63/Henryk_sienkiewicz_by_kazimierz_pochwalski.png/170px-Henryk_sienkiewicz_by_kazimierz_pochwalski.png" decoding="async" width="170" height="227" class="thumbimage" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/6/63/Henryk_sienkiewicz_by_kazimierz_pochwalski.png/255px-Henryk_sienkiewicz_by_kazimierz_pochwalski.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/6/63/Henryk_sienkiewicz_by_kazimierz_pochwalski.png/340px-Henryk_sienkiewicz_by_kazimierz_pochwalski.png 2x" data-file-width="554" data-file-height="740"></a>  <div class="thumbcaption"><div class="magnify"><a href="/wiki/File:Henryk_sienkiewicz_by_kazimierz_pochwalski.png" class="internal" title="Enlarge"></a></div><a href="/wiki/Henryk_Sienkiewicz" title="Henryk Sienkiewicz">Henryk Sienkiewicz</a>, famous Polish novelist</div></div></div>
<p>Almost no Polish literature remains before <a href="/wiki/Christianity" title="Christianity">Christianisation</a> in the <a href="/wiki/10th_century" title="10th century">10th century</a>. Polish literature was written in the <a href="/wiki/Latin_language" class="mw-redirect" title="Latin language">Latin language</a> during the <a href="/wiki/Middle_Ages" title="Middle Ages">Middle Ages</a>. The <a href="/wiki/Polish_language" title="Polish language">Polish language</a> was accepted as equal to Latin after the <a href="/wiki/Renaissance" title="Renaissance">Renaissance</a> for literature.
</p><p><a href="/wiki/Jan_Kochanowski" title="Jan Kochanowski">Jan Kochanowski</a> was a leading poet of <a href="/wiki/Renaissance" title="Renaissance">European Renaissance</a> literature in the <a href="/wiki/16th_century" title="16th century">16th century</a>. Other great Polish poets include <a href="/wiki/Adam_Mickiewicz" title="Adam Mickiewicz">Adam Mickiewicz</a> who wrote <i><a href="/wiki/Sir_Thaddeus" title="Sir Thaddeus">Pan Tadeusz</a></i> epic in 1834.
</p><p>Several Polish novelists have won the Nobel prize. <a href="/wiki/Henryk_Sienkiewicz" title="Henryk Sienkiewicz">Henryk Sienkiewicz</a> won in 19 dramatized versions of famous events in Polish history. <a href="/wiki/W%C5%82adys%C5%82aw_Reymont" title="Władysław Reymont">Władysław Reymont</a> won a Nobel prize in 1924. He wrote the novel <a href="/w/index.php?title=Ch%C5%82opi&amp;action=edit&amp;redlink=1" class="new" title="Chłopi (not yet started)">Chłopi</a>. Two polish poets won Nobel prizes as well. One is <a href="/wiki/Wis%C5%82awa_Szymborska" title="Wisława Szymborska">Wisława Szymborska</a> (1996) and the second <a href="/w/index.php?title=Czes%C5%82aw_Mi%C5%82osz&amp;action=edit&amp;redlink=1" class="new" title="Czesław Miłosz (not yet started)">Czesław Miłosz</a> (1980).
</p><p><a href="/wiki/Stanis%C5%82aw_Lem" class="mw-redirect" title="Stanisław Lem">Stanisław Lem</a> is a famous <a href="/wiki/Science_fiction" title="Science fiction">science fiction</a> author in the modern era. His <i><a href="/w/index.php?title=Solaris_(novel)&amp;action=edit&amp;redlink=1" class="new" title="Solaris (novel) (not yet started)">Solaris</a></i> novel was made twice into a feature <a href="/wiki/Movie" title="Movie">film</a>.
</p>
<h2><span class="mw-headline" id="People">People</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Poland&amp;veaction=edit&amp;section=10" class="mw-editsection-visualeditor" title="Change section: People">change</a><span class="mw-editsection-divider"> | </span><a href="/w/index.php?title=Poland&amp;action=edit&amp;section=10" title="Change section: People">change source</a><span class="mw-editsection-bracket">]</span></span></h2>
<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r7707418"><div role="note" class="hatnote navigation-not-searchable">Main article: <a href="/wiki/Poles" title="Poles">Poles</a></div>
<div class="thumb tleft"><div class="thumbinner" style="width:172px;"><a href="/wiki/File:Chopin,_by_Wodzinska.JPG" class="image"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/3/33/Chopin%2C_by_Wodzinska.JPG/170px-Chopin%2C_by_Wodzinska.JPG" decoding="async" width="170" height="229" class="thumbimage" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/3/33/Chopin%2C_by_Wodzinska.JPG/255px-Chopin%2C_by_Wodzinska.JPG 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/3/33/Chopin%2C_by_Wodzinska.JPG/340px-Chopin%2C_by_Wodzinska.JPG 2x" data-file-width="1584" data-file-height="2136"></a>  <div class="thumbcaption"><div class="magnify"><a href="/wiki/File:Chopin,_by_Wodzinska.JPG" class="internal" title="Enlarge"></a></div><a href="/wiki/Frederic_Chopin" class="mw-redirect" title="Frederic Chopin">Frederic Chopin</a>, famous Polish composer and pianist</div></div></div>
<p>In the past, Poland was inhabited by people from different nations and of different religions (mainly <a href="/wiki/Roman_Catholicism" class="mw-redirect" title="Roman Catholicism">Catholics</a>, <a href="/wiki/Eastern_Orthodox_Church" title="Eastern Orthodox Church">Orthodox</a> and <a href="/wiki/Judaism" title="Judaism">Judaism</a>). This changed after 1939, because of the <a href="/wiki/Nazism" title="Nazism">Nazi</a> <a href="/wiki/Holocaust" class="mw-redirect" title="Holocaust">Holocaust</a> which killed many Polish Jews. After <a href="/wiki/World_War_II" title="World War II">World War II</a>, the country was changed into a <a href="/wiki/Communism" title="Communism">communist</a> country, by the <a href="/wiki/Warsaw_Pact" title="Warsaw Pact">Warsaw Pact</a> which included most central European countries and Russia <a href="/wiki/Russia" title="Russia">Russia</a>.
</p><p>Today 38,038,000 people live in Poland (2011). In 2002 96.74% of the population call themselves Polish, while 471,500 people (1.23%) claimed another nationality. 774,900 people (2.03%) did not declare any nationality. Nationalities, or <a href="/wiki/Ethnicity" class="mw-redirect" title="Ethnicity">ethnic groups</a> in Poland are <a href="/w/index.php?title=Silesians&amp;action=edit&amp;redlink=1" class="new" title="Silesians (not yet started)">Silesians</a>, <a href="/wiki/Germans" title="Germans">Germans</a> (most in the former <a href="/wiki/Opole_Voivodeship" title="Opole Voivodeship">Opole Voivodeship</a>), <a href="/wiki/Ukraine" title="Ukraine">Ukrainians</a>, <a href="/wiki/Lithuania" title="Lithuania">Lithuanians</a>, <a href="/wiki/Russia" title="Russia">Russians</a>, <a href="/wiki/Jew" title="Jew">Jews</a> and <a href="/wiki/Belarus" title="Belarus">Belarusians</a>. The <a href="/wiki/Polish_language" title="Polish language">Polish language</a> is part of the <a href="/wiki/West_Slavs" title="West Slavs">West Slavic</a> section of the <a href="/wiki/Slavic_languages" title="Slavic languages">Slavic languages</a>. It is also the <a href="/wiki/Official_language" title="Official language">official language</a> of Poland. <a href="/wiki/English_language" title="English language">English</a> and <a href="/wiki/German_language" title="German language">German</a> are the most common second languages studied and spoken.
</p>
<div class="thumb tright"><div class="thumbinner" style="width:172px;"><a href="/wiki/File:Madame_curie_3334194920_e4014f35a4_o.jpg" class="image"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/6/63/Madame_curie_3334194920_e4014f35a4_o.jpg/170px-Madame_curie_3334194920_e4014f35a4_o.jpg" decoding="async" width="170" height="226" class="thumbimage" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/6/63/Madame_curie_3334194920_e4014f35a4_o.jpg/255px-Madame_curie_3334194920_e4014f35a4_o.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/6/63/Madame_curie_3334194920_e4014f35a4_o.jpg/340px-Madame_curie_3334194920_e4014f35a4_o.jpg 2x" data-file-width="583" data-file-height="776"></a>  <div class="thumbcaption"><div class="magnify"><a href="/wiki/File:Madame_curie_3334194920_e4014f35a4_o.jpg" class="internal" title="Enlarge"></a></div><a href="/wiki/Marie_Curie" title="Marie Curie">Marie Curie</a>, famous Polish chemist and two time Nobel Prize winner</div></div></div>
<p>In the past few years, Poland's population has gone down because of an increase in <a href="/wiki/Emigrate" class="mw-redirect" title="Emigrate">emigration</a> and a sharp drop in the birth rate. In 2006, the census office estimated the total population of Poland at 38,536,869, a very small rise from the 2002 figure of 38,230,080. Since Poland's accession to the <a href="/wiki/European_Union" title="European Union">European Union</a>, many Polish people have moved to work in Western European countries like the <a href="/wiki/United_Kingdom" title="United Kingdom">United Kingdom</a> and the <a href="/wiki/Republic_of_Ireland" title="Republic of Ireland">Republic of Ireland</a>. Some organizations state people have left because of high <a href="/wiki/Unemployment" title="Unemployment">unemployment</a> (10.5%) and better opportunities for work somewhere else. In April 2007, the Polish population of the <a href="/wiki/United_Kingdom" title="United Kingdom">United Kingdom</a> had risen to about 300,000 people and estimates predict about 65,000 Polish people living in the <a href="/wiki/Republic_of_Ireland" title="Republic of Ireland">Republic of Ireland</a>. However, in recent years strong growth of the Polish economy and the increasing value of Polish currency (PLN) makes many Polish immigrants go back home. In 2007, the number of people leaving the country was lower than people who are coming back. Poland became an attractive place to work for people from other countries (mainly Ukraine).
</p><p>A Polish minority is still present in neighboring countries of Ukraine, Belarus, and Lithuania, as well as in other countries. The largest number of ethnic Poles outside of the country can be found in the <a href="/wiki/United_States" title="United States">United States</a>.
</p>
<h2><span class="mw-headline" id="Famous_people">Famous people</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Poland&amp;veaction=edit&amp;section=11" class="mw-editsection-visualeditor" title="Change section: Famous people">change</a><span class="mw-editsection-divider"> | </span><a href="/w/index.php?title=Poland&amp;action=edit&amp;section=11" title="Change section: Famous people">change source</a><span class="mw-editsection-bracket">]</span></span></h2>
<ul><li><a href="/wiki/Fr%C3%A9d%C3%A9ric_Chopin" title="Frédéric Chopin">Fryderyk Chopin</a>, a music composer.</li>
<li><a href="/wiki/Joseph_Conrad" title="Joseph Conrad">Joseph Conrad</a>, born Józef Teodor Konrad Korzeniowski, an acclaimed author who however wrote in English.</li>
<li><a href="/wiki/Nicolaus_Copernicus" title="Nicolaus Copernicus">Nicolaus Copernicus</a>, an <a href="/wiki/Astronomer" title="Astronomer">astronomer</a> who showed that the <a href="/wiki/Earth" title="Earth">Earth</a> moves around the <a href="/wiki/Sun" title="Sun">Sun</a>.</li>
<li><a href="/wiki/Marie_Curie" title="Marie Curie">Maria Skłodowska-Curie</a> discovered <a href="/wiki/Radium" title="Radium">radium</a> and <a href="/wiki/Polonium" title="Polonium">polonium</a>.</li>
<li><a href="/w/index.php?title=Franciszek_Kamie%C5%84ski&amp;action=edit&amp;redlink=1" class="new" title="Franciszek Kamieński (not yet started)">Franciszek Kamieński</a>, discovered <a href="/wiki/Mycorrhiza" title="Mycorrhiza">mycorrhiza</a>.</li>
<li><a href="/wiki/Tadeusz_Ko%C5%9Bciuszko" title="Tadeusz Kościuszko">Tadeusz Kościuszko</a>, an army commander who fought for <a href="/wiki/United_States" title="United States">USA</a>'s and Poland's independence.</li>
<li><a href="/wiki/Robert_Kubica" title="Robert Kubica">Robert Kubica</a>, a <a href="/wiki/Formula_1" title="Formula 1">F1</a> driver.</li>
<li><a href="/wiki/Stanis%C5%82aw_Lem" class="mw-redirect" title="Stanisław Lem">Stanisław Lem</a>, a <a href="/wiki/Science_fiction" title="Science fiction">science fiction</a> writer.</li>
<li><a href="/wiki/Adam_Ma%C5%82ysz" title="Adam Małysz">Adam Małysz</a>, a ski-jumper.</li>
<li><a href="/wiki/Adam_Mickiewicz" title="Adam Mickiewicz">Adam Mickiewicz</a>, a <a href="/wiki/Poet" title="Poet">poet</a></li>
<li><a href="/wiki/Pope_John_Paul_II" title="Pope John Paul II">Pope John Paul II</a> (earlier Karol Wojtyła). Before he became Pope, he was a <a href="/wiki/Bishop" title="Bishop">Bishop</a> in <a href="/wiki/Krak%C3%B3w" title="Kraków">Kraków</a>.</li>
<li><a href="/wiki/Agnieszka_Radwa%C5%84ska" title="Agnieszka Radwańska">Agnieszka Radwańska</a>, female tennis player</li>
<li><a href="/wiki/W%C5%82adys%C5%82aw_Reymont" title="Władysław Reymont">Władysław Reymont</a>, a <a href="/wiki/Novelist" class="mw-redirect" title="Novelist">novelist</a></li>
<li><a href="/wiki/Henryk_Sienkiewicz" title="Henryk Sienkiewicz">Henryk Sienkiewicz</a>, a novelist</li>
<li><a href="/w/index.php?title=Kamil_Stoch&amp;action=edit&amp;redlink=1" class="new" title="Kamil Stoch (not yet started)">Kamil Stoch</a>, a ski jumper</li>
<li><a href="/wiki/Wis%C5%82awa_Szymborska" title="Wisława Szymborska">Wisława Szymborska</a>, a <a href="/wiki/Writer" title="Writer">writer</a></li>
<li><a href="/wiki/Andrzej_Wajda" title="Andrzej Wajda">Andrzej Wajda</a>, a <a href="/wiki/Film_director" class="mw-redirect" title="Film director">film director</a></li>
<li><a href="/wiki/Lech_Wa%C5%82%C4%99sa" title="Lech Wałęsa">Lech Wałęsa</a>, leader of "Solidarność" ("Solidarity"), he helped defeat the communist government in Poland and <a href="/wiki/USSR" class="mw-redirect" title="USSR">USSR</a> influence in Central and Eastern Europe</li>
<li><a href="/wiki/Robert_Lewandowski" title="Robert Lewandowski">Robert Lewandowski</a>, a football player</li>
<li><a href="/w/index.php?title=Czes%C5%82aw_Mi%C5%82osz&amp;action=edit&amp;redlink=1" class="new" title="Czesław Miłosz (not yet started)">Czesław Miłosz</a>, a <a href="/wiki/Poet" title="Poet">poet</a></li>
<li><a href="/wiki/Jan_Matejko" title="Jan Matejko">Jan Matejko</a>, a <a href="/wiki/Painter" class="mw-redirect" title="Painter">painter</a></li></ul>
<h2><span class="mw-headline" id="Urban_demographics">Urban demographics</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Poland&amp;veaction=edit&amp;section=12" class="mw-editsection-visualeditor" title="Change section: Urban demographics">change</a><span class="mw-editsection-divider"> | </span><a href="/w/index.php?title=Poland&amp;action=edit&amp;section=12" title="Change section: Urban demographics">change source</a><span class="mw-editsection-bracket">]</span></span></h2>
<div class="thumb tright"><div class="thumbinner" style="width:202px;"><a href="/wiki/File:Lotnicza_panorama_Warszawy.jpg" class="image"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Lotnicza_panorama_Warszawy.jpg/200px-Lotnicza_panorama_Warszawy.jpg" decoding="async" width="200" height="124" class="thumbimage" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Lotnicza_panorama_Warszawy.jpg/300px-Lotnicza_panorama_Warszawy.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Lotnicza_panorama_Warszawy.jpg/400px-Lotnicza_panorama_Warszawy.jpg 2x" data-file-width="3884" data-file-height="2402"></a>  <div class="thumbcaption"><div class="magnify"><a href="/wiki/File:Lotnicza_panorama_Warszawy.jpg" class="internal" title="Enlarge"></a></div><a href="/wiki/Warsaw" title="Warsaw">Warsaw</a></div></div></div>
<div class="thumb tright"><div class="thumbinner" style="width:202px;"><a href="/wiki/File:A-10_Sukiennice_w_Krakowie_Krak%C3%B3w,_Rynek_G%C5%82%C3%B3wny_MM.jpg" class="image"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/A-10_Sukiennice_w_Krakowie_Krak%C3%B3w%2C_Rynek_G%C5%82%C3%B3wny_MM.jpg/200px-A-10_Sukiennice_w_Krakowie_Krak%C3%B3w%2C_Rynek_G%C5%82%C3%B3wny_MM.jpg" decoding="async" width="200" height="134" class="thumbimage" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/A-10_Sukiennice_w_Krakowie_Krak%C3%B3w%2C_Rynek_G%C5%82%C3%B3wny_MM.jpg/300px-A-10_Sukiennice_w_Krakowie_Krak%C3%B3w%2C_Rynek_G%C5%82%C3%B3wny_MM.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/be/A-10_Sukiennice_w_Krakowie_Krak%C3%B3w%2C_Rynek_G%C5%82%C3%B3wny_MM.jpg/400px-A-10_Sukiennice_w_Krakowie_Krak%C3%B3w%2C_Rynek_G%C5%82%C3%B3wny_MM.jpg 2x" data-file-width="2896" data-file-height="1944"></a>  <div class="thumbcaption"><div class="magnify"><a href="/wiki/File:A-10_Sukiennice_w_Krakowie_Krak%C3%B3w,_Rynek_G%C5%82%C3%B3wny_MM.jpg" class="internal" title="Enlarge"></a></div><a href="/wiki/Krak%C3%B3w" title="Kraków">Kraków</a></div></div></div>
<div class="thumb tright"><div class="thumbinner" style="width:202px;"><a href="/wiki/File:Old_marketplace_and_city_hall_in_Pozna%C5%84.jpg" class="image"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Old_marketplace_and_city_hall_in_Pozna%C5%84.jpg/200px-Old_marketplace_and_city_hall_in_Pozna%C5%84.jpg" decoding="async" width="200" height="139" class="thumbimage" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Old_marketplace_and_city_hall_in_Pozna%C5%84.jpg/300px-Old_marketplace_and_city_hall_in_Pozna%C5%84.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Old_marketplace_and_city_hall_in_Pozna%C5%84.jpg/400px-Old_marketplace_and_city_hall_in_Pozna%C5%84.jpg 2x" data-file-width="3279" data-file-height="2274"></a>  <div class="thumbcaption"><div class="magnify"><a href="/wiki/File:Old_marketplace_and_city_hall_in_Pozna%C5%84.jpg" class="internal" title="Enlarge"></a></div><a href="/wiki/Pozna%C5%84" title="Poznań">Poznań</a></div></div></div>
<div class="thumb tright"><div class="thumbinner" style="width:202px;"><a href="/wiki/File:Wroc%C5%82aw_-_Rynek_2015-12-25_12-44-18.JPG" class="image"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/28/Wroc%C5%82aw_-_Rynek_2015-12-25_12-44-18.JPG/200px-Wroc%C5%82aw_-_Rynek_2015-12-25_12-44-18.JPG" decoding="async" width="200" height="133" class="thumbimage" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/28/Wroc%C5%82aw_-_Rynek_2015-12-25_12-44-18.JPG/300px-Wroc%C5%82aw_-_Rynek_2015-12-25_12-44-18.JPG 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/28/Wroc%C5%82aw_-_Rynek_2015-12-25_12-44-18.JPG/400px-Wroc%C5%82aw_-_Rynek_2015-12-25_12-44-18.JPG 2x" data-file-width="3008" data-file-height="2000"></a>  <div class="thumbcaption"><div class="magnify"><a href="/wiki/File:Wroc%C5%82aw_-_Rynek_2015-12-25_12-44-18.JPG" class="internal" title="Enlarge"></a></div><a href="/wiki/Wroc%C5%82aw" title="Wrocław">Wrocław</a></div></div></div>
<div class="thumb tright"><div class="thumbinner" style="width:202px;"><a href="/wiki/File:Orion_Business_Tower_-_poziom.jpg" class="image"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/1/14/Orion_Business_Tower_-_poziom.jpg/200px-Orion_Business_Tower_-_poziom.jpg" decoding="async" width="200" height="133" class="thumbimage" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/14/Orion_Business_Tower_-_poziom.jpg/300px-Orion_Business_Tower_-_poziom.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/14/Orion_Business_Tower_-_poziom.jpg/400px-Orion_Business_Tower_-_poziom.jpg 2x" data-file-width="1404" data-file-height="936"></a>  <div class="thumbcaption"><div class="magnify"><a href="/wiki/File:Orion_Business_Tower_-_poziom.jpg" class="internal" title="Enlarge"></a></div><a href="/wiki/%C5%81%C3%B3d%C5%BA" title="Łódź">Łódź</a></div></div></div>
<div class="thumb tright"><div class="thumbinner" style="width:202px;"><a href="/wiki/File:Gdansk_Glowne_Miasto.jpg" class="image"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Gdansk_Glowne_Miasto.jpg/200px-Gdansk_Glowne_Miasto.jpg" decoding="async" width="200" height="110" class="thumbimage" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Gdansk_Glowne_Miasto.jpg/300px-Gdansk_Glowne_Miasto.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Gdansk_Glowne_Miasto.jpg/400px-Gdansk_Glowne_Miasto.jpg 2x" data-file-width="799" data-file-height="439"></a>  <div class="thumbcaption"><div class="magnify"><a href="/wiki/File:Gdansk_Glowne_Miasto.jpg" class="internal" title="Enlarge"></a></div><a href="/wiki/Gda%C5%84sk" title="Gdańsk">Gdańsk</a></div></div></div>
<div class="thumb tright"><div class="thumbinner" style="width:202px;"><a href="/wiki/File:2009-05-30-polska-by-RalfR-30.jpg" class="image"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b9/2009-05-30-polska-by-RalfR-30.jpg/200px-2009-05-30-polska-by-RalfR-30.jpg" decoding="async" width="200" height="133" class="thumbimage" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b9/2009-05-30-polska-by-RalfR-30.jpg/300px-2009-05-30-polska-by-RalfR-30.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b9/2009-05-30-polska-by-RalfR-30.jpg/400px-2009-05-30-polska-by-RalfR-30.jpg 2x" data-file-width="3008" data-file-height="2000"></a>  <div class="thumbcaption"><div class="magnify"><a href="/wiki/File:2009-05-30-polska-by-RalfR-30.jpg" class="internal" title="Enlarge"></a></div><a href="/wiki/Szczecin" title="Szczecin">Szczecin</a></div></div></div>
<div class="thumb tright"><div class="thumbinner" style="width:202px;"><a href="/wiki/File:Katowice_Rynek.jpg" class="image"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Katowice_Rynek.jpg/200px-Katowice_Rynek.jpg" decoding="async" width="200" height="132" class="thumbimage" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Katowice_Rynek.jpg/300px-Katowice_Rynek.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Katowice_Rynek.jpg/400px-Katowice_Rynek.jpg 2x" data-file-width="4810" data-file-height="3186"></a>  <div class="thumbcaption"><div class="magnify"><a href="/wiki/File:Katowice_Rynek.jpg" class="internal" title="Enlarge"></a></div><a href="/wiki/Katowice" title="Katowice">Katowice</a></div></div></div>
<p>The lists below show the population count of Poland's largest cities based on 2005 estimates.
</p>
<table class="wikitable">

<tbody><tr bgcolor="#DDDDDD">
<th>&nbsp;&nbsp;
</th>
<th><a href="/wiki/Agglomeration" class="mw-redirect" title="Agglomeration">Agglomeration</a> or <a href="/wiki/Conurbation" title="Conurbation">conurbation</a>
</th>
<th>&nbsp;Voivodeship&nbsp;
</th>
<th>Inhabitants <br>(Estimated, 2005)
</th></tr>
<tr>
<td align="left">1</td>
<td><a href="/wiki/Katowice" title="Katowice">Katowice</a> (<a href="/w/index.php?title=Upper_Silesian_Industrial_Area&amp;action=edit&amp;redlink=1" class="new" title="Upper Silesian Industrial Area (not yet started)">USIA</a>)</td>
<td><a href="/wiki/Silesian_Voivodeship" title="Silesian Voivodeship">Silesia</a></td>
<td align="right"><b>3,487,000</b>
</td></tr>
<tr>
<td align="right">2</td>
<td><a href="/wiki/Warsaw" title="Warsaw">Warsaw</a> (Warszawa)</td>
<td><a href="/wiki/Masovian_Voivodeship" title="Masovian Voivodeship">Masovia</a></td>
<td align="right">2,679,000
</td></tr>
<tr>
<td align="right">3</td>
<td><a href="/wiki/Krak%C3%B3w" title="Kraków">Kraków</a></td>
<td><a href="/wiki/Lesser_Poland_Voivodeship" title="Lesser Poland Voivodeship">Lesser Poland</a></td>
<td align="right">1,400,000
</td></tr>
<tr>
<td align="right">4</td>
<td><a href="/wiki/%C5%81%C3%B3d%C5%BA" title="Łódź">Łódź</a></td>
<td><a href="/wiki/%C5%81%C3%B3d%C5%BA_Voivodeship" title="Łódź Voivodeship">Łódź</a></td>
<td align="right">1,300,000
</td></tr>
<tr>
<td align="right">5</td>
<td><a href="/wiki/Tricity" title="Tricity">Tricity</a></td>
<td><a href="/wiki/Pomeranian_Voivodeship" title="Pomeranian Voivodeship">Pomerania</a></td>
<td align="right">1,100,000
</td></tr>
<tr>
<td align="right">6</td>
<td><a href="/wiki/Pozna%C5%84" title="Poznań">Poznań</a></td>
<td><a href="/wiki/Greater_Poland_Voivodeship" title="Greater Poland Voivodeship">Greater Poland</a></td>
<td align="right">1,000,000
</td></tr>
</tbody></table>
<table class="wikitable">

<tbody><tr bgcolor="#DDDDDD">
<th>&nbsp;&nbsp;
</th>
<th>City
</th>
<th>&nbsp;Voivodeship&nbsp;
</th>
<th>Inhabitants<br>May 20, 2002
</th>
<th>Inhabitants<br>December 31, 2004
</th></tr>
<tr>
<td align="left">1</td>
<td><a href="/wiki/Warsaw" title="Warsaw">Warsaw</a> (Warszawa)</td>
<td><a href="/wiki/Masovian_Voivodeship" title="Masovian Voivodeship">Masovia</a></td>
<td align="right"><b>1,671,670</b></td>
<td align="right"><b>1,692,854</b>
</td></tr>
<tr>
<td align="left">2</td>
<td><a href="/wiki/%C5%81%C3%B3d%C5%BA" title="Łódź">Łódź</a></td>
<td><a href="/wiki/%C5%81%C3%B3d%C5%BA_Voivodeship" title="Łódź Voivodeship">Łódź</a></td>
<td align="right">789,318</td>
<td align="right">774,004
</td></tr>
<tr>
<td align="left">3</td>
<td><a href="/wiki/Krak%C3%B3w" title="Kraków">Kraków</a></td>
<td><a href="/wiki/Lesser_Poland_Voivodeship" title="Lesser Poland Voivodeship">Lesser Poland</a></td>
<td align="right">758,544</td>
<td align="right">757,430
</td></tr>
<tr>
<td align="right">4</td>
<td><a href="/wiki/Wroc%C5%82aw" title="Wrocław">Wrocław</a></td>
<td><a href="/wiki/Lower_Silesian_Voivodeship" title="Lower Silesian Voivodeship">Lower Silesia</a></td>
<td align="right">640,367</td>
<td align="right">636,268
</td></tr>
<tr>
<td align="right">5</td>
<td><a href="/wiki/Pozna%C5%84" title="Poznań">Poznań</a></td>
<td><a href="/wiki/Greater_Poland_Voivodeship" title="Greater Poland Voivodeship">Greater Poland</a></td>
<td align="right">578,886</td>
<td align="right">570,778
</td></tr>
<tr>
<td align="right">6</td>
<td><a href="/wiki/Gda%C5%84sk" title="Gdańsk">Gdańsk</a></td>
<td><a href="/wiki/Pomeranian_Voivodeship" title="Pomeranian Voivodeship">Pomerania</a></td>
<td align="right">461,334</td>
<td align="right">459,072
</td></tr>
<tr>
<td align="right">7</td>
<td><a href="/wiki/Szczecin" title="Szczecin">Szczecin</a></td>
<td><a href="/wiki/West_Pomeranian_Voivodeship" title="West Pomeranian Voivodeship">Western Pomerania</a></td>
<td align="right">415,399</td>
<td align="right">411,900
</td></tr>
<tr>
<td align="right">8</td>
<td><a href="/wiki/Bydgoszcz" title="Bydgoszcz">Bydgoszcz</a></td>
<td><a href="/wiki/Kuyavian-Pomeranian_Voivodeship" title="Kuyavian-Pomeranian Voivodeship">Kuyavia-Pomerania</a></td>
<td align="right">373,804</td>
<td align="right">368,235
</td></tr>
<tr>
<td align="right">9</td>
<td><a href="/wiki/Lublin" title="Lublin">Lublin</a></td>
<td><a href="/wiki/Lublin_Voivodeship" title="Lublin Voivodeship">Lublin</a></td>
<td align="right">357,110</td>
<td align="right">355,998
</td></tr>
<tr>
<td align="right">10</td>
<td><a href="/wiki/Katowice" title="Katowice">Katowice</a></td>
<td><a href="/wiki/Silesian_Voivodeship" title="Silesian Voivodeship">Silesia</a></td>
<td align="right">327,222</td>
<td align="right">319,904
</td></tr>
<tr>
<td align="right">11</td>
<td><a href="/wiki/Bia%C5%82ystok" title="Białystok">Białystok</a></td>
<td><a href="/w/index.php?title=Podlasie_Voivodeship&amp;action=edit&amp;redlink=1" class="new" title="Podlasie Voivodeship (not yet started)">Podlasie</a></td>
<td align="right">291,383</td>
<td align="right">292,150
</td></tr>
<tr>
<td align="right">12</td>
<td><a href="/wiki/Gdynia" title="Gdynia">Gdynia</a></td>
<td><a href="/wiki/Pomeranian_Voivodeship" title="Pomeranian Voivodeship">Pomerania</a></td>
<td align="right">253,458</td>
<td align="right">253,324
</td></tr>
<tr>
<td align="right">13</td>
<td><a href="/wiki/Cz%C4%99stochowa" class="mw-redirect" title="Częstochowa">Częstochowa</a></td>
<td><a href="/wiki/Silesian_Voivodeship" title="Silesian Voivodeship">Silesia</a></td>
<td align="right">251,436</td>
<td align="right">248,032
</td></tr>
<tr>
<td align="right">14</td>
<td><a href="/wiki/Sosnowiec" title="Sosnowiec">Sosnowiec</a></td>
<td><a href="/wiki/Silesian_Voivodeship" title="Silesian Voivodeship">Silesia</a></td>
<td align="right">232,622</td>
<td align="right">228,192
</td></tr>
<tr>
<td align="right">15</td>
<td><a href="/wiki/Radom" title="Radom">Radom</a></td>
<td><a href="/wiki/Masovian_Voivodeship" title="Masovian Voivodeship">Masovia</a></td>
<td align="right">229,699</td>
<td align="right">227,613
</td></tr>
<tr>
<td align="right">16</td>
<td><a href="/wiki/Kielce" title="Kielce">Kielce</a></td>
<td><a href="/wiki/%C5%9Awi%C4%99tokrzyskie_Voivodeship" title="Świętokrzyskie Voivodeship">Świętokrzyskie</a></td>
<td align="right">212,429</td>
<td align="right">209,455
</td></tr>
<tr>
<td align="right">17</td>
<td><a href="/wiki/Toru%C5%84" title="Toruń">Toruń</a></td>
<td><a href="/wiki/Kuyavian-Pomeranian_Voivodeship" title="Kuyavian-Pomeranian Voivodeship">Kuyavia-Pomerania</a></td>
<td align="right">211,243</td>
<td align="right">208,278
</td></tr>
<tr>
<td align="right">18</td>
<td><a href="/wiki/Gliwice" title="Gliwice">Gliwice</a></td>
<td><a href="/wiki/Silesian_Voivodeship" title="Silesian Voivodeship">Silesia</a></td>
<td align="right">203,814</td>
<td align="right">200,361
</td></tr>
<tr>
<td align="right">19</td>
<td><a href="/wiki/Zabrze" title="Zabrze">Zabrze</a></td>
<td><a href="/wiki/Silesian_Voivodeship" title="Silesian Voivodeship">Silesia</a></td>
<td align="right">195,293</td>
<td align="right">192,546
</td></tr>
<tr>
<td align="right">20</td>
<td><a href="/wiki/Bytom" title="Bytom">Bytom</a></td>
<td><a href="/wiki/Silesian_Voivodeship" title="Silesian Voivodeship">Silesia</a></td>
<td align="right">193,546</td>
<td align="right">189,535
</td></tr>
<tr>
<td align="right">21</td>
<td><a href="/wiki/Bielsko-Bia%C5%82a" title="Bielsko-Biała">Bielsko-Biała</a></td>
<td><a href="/wiki/Silesian_Voivodeship" title="Silesian Voivodeship">Silesia</a></td>
<td align="right">178,028</td>
<td align="right">176,987
</td></tr>
<tr>
<td align="right">22</td>
<td><a href="/wiki/Olsztyn" title="Olsztyn">Olsztyn</a></td>
<td><a href="/wiki/Warmian-Masurian_Voivodeship" title="Warmian-Masurian Voivodeship">Warmia-Masuria</a></td>
<td align="right">173,102</td>
<td align="right">174,550
</td></tr>
<tr>
<td align="right">23</td>
<td><a href="/wiki/Rzesz%C3%B3w" title="Rzeszów">Rzeszów</a></td>
<td><a href="/wiki/Subcarpathian_Voivodeship" class="mw-redirect" title="Subcarpathian Voivodeship">Subcarpathia</a></td>
<td align="right">160,376</td>
<td align="right">159,020
</td></tr>
<tr>
<td align="right">24</td>
<td><a href="/wiki/Ruda_%C5%9Al%C4%85ska" title="Ruda Śląska">Ruda Śląska</a></td>
<td><a href="/wiki/Silesian_Voivodeship" title="Silesian Voivodeship">Silesia</a></td>
<td align="right">150,595</td>
<td align="right">147,403
</td></tr>
<tr>
<td align="right">25</td>
<td><a href="/wiki/Rybnik" title="Rybnik">Rybnik</a></td>
<td><a href="/wiki/Silesian_Voivodeship" title="Silesian Voivodeship">Silesia</a></td>
<td align="right">142,731</td>
<td align="right">141,755
</td></tr>
<tr>
<td align="right">26</td>
<td><a href="/wiki/Tychy" title="Tychy">Tychy</a></td>
<td><a href="/wiki/Silesian_Voivodeship" title="Silesian Voivodeship">Silesia</a></td>
<td align="right">132,816</td>
<td align="right">131,547
</td></tr>
<tr>
<td align="right">27</td>
<td><a href="/wiki/D%C4%85browa_G%C3%B3rnicza" title="Dąbrowa Górnicza">Dąbrowa Górnicza</a></td>
<td><a href="/wiki/Silesian_Voivodeship" title="Silesian Voivodeship">Silesia</a></td>
<td align="right">132,236</td>
<td align="right">130,789
</td></tr>
<tr>
<td align="right">28</td>
<td><a href="/wiki/Opole" title="Opole">Opole</a></td>
<td><a href="/wiki/Opole_Voivodeship" title="Opole Voivodeship">Opole</a></td>
<td align="right">129,946</td>
<td align="right">128,864
</td></tr>
<tr>
<td align="right">29</td>
<td><a href="/wiki/P%C5%82ock" title="Płock">Płock</a></td>
<td><a href="/wiki/Masovian_Voivodeship" title="Masovian Voivodeship">Masovia</a></td>
<td align="right">128,361</td>
<td align="right">127,841
</td></tr>
<tr>
<td align="right">30</td>
<td><a href="/wiki/Elbl%C4%85g" title="Elbląg">Elbląg</a></td>
<td><a href="/wiki/Warmian-Masurian_Voivodeship" title="Warmian-Masurian Voivodeship">Warmia-Masuria</a></td>
<td align="right">128,134</td>
<td align="right">127,655
</td></tr>
<tr>
<td align="right">31</td>
<td><a href="/wiki/Wa%C5%82brzych" title="Wałbrzych">Wałbrzych</a></td>
<td><a href="/wiki/Lower_Silesian_Voivodeship" title="Lower Silesian Voivodeship">Lower Silesia</a></td>
<td align="right">130,268</td>
<td align="right">127,566
</td></tr>
<tr>
<td align="right">32</td>
<td><a href="/wiki/Gorz%C3%B3w_Wielkopolski" title="Gorzów Wielkopolski">Gorzów Wielkopolski</a></td>
<td><a href="/wiki/Lubusz_Voivodeship" title="Lubusz Voivodeship">Lubusz</a></td>
<td align="right">125,914</td>
<td align="right">125,578
</td></tr>
<tr>
<td align="right">33</td>
<td><a href="/wiki/W%C5%82oc%C5%82awek" title="Włocławek">Włocławek</a></td>
<td><a href="/wiki/Kuyavian-Pomeranian_Voivodeship" title="Kuyavian-Pomeranian Voivodeship">Kuyavia-Pomerania</a></td>
<td align="right">121,229</td>
<td align="right">120,369
</td></tr>
<tr>
<td align="right">34</td>
<td><a href="/wiki/Tarn%C3%B3w" title="Tarnów">Tarnów</a></td>
<td><a href="/wiki/Lesser_Poland_Voivodeship" title="Lesser Poland Voivodeship">Lesser Poland</a></td>
<td align="right">119,913</td>
<td align="right">118,267
</td></tr>
<tr>
<td align="right">35</td>
<td><a href="/wiki/Zielona_G%C3%B3ra" title="Zielona Góra">Zielona Góra</a></td>
<td><a href="/wiki/Lubusz_Voivodeship" title="Lubusz Voivodeship">Lubusz</a></td>
<td align="right">118,293</td>
<td align="right">118,516
</td></tr>
<tr>
<td align="right">36</td>
<td><a href="/wiki/Chorz%C3%B3w" title="Chorzów">Chorzów</a></td>
<td><a href="/wiki/Silesian_Voivodeship" title="Silesian Voivodeship">Silesia</a></td>
<td align="right">117,430</td>
<td align="right">115,241
</td></tr>
<tr>
<td align="right">37</td>
<td><a href="/wiki/Kalisz" title="Kalisz">Kalisz</a></td>
<td><a href="/wiki/Greater_Poland_Voivodeship" title="Greater Poland Voivodeship">Greater Poland</a></td>
<td align="right">109,498</td>
<td align="right">108,792
</td></tr>
<tr>
<td align="right">38</td>
<td><a href="/wiki/Koszalin" title="Koszalin">Koszalin</a></td>
<td><a href="/wiki/West_Pomeranian_Voivodeship" title="West Pomeranian Voivodeship">Western Pomerania</a></td>
<td align="right">108,709</td>
<td align="right">107,773
</td></tr>
<tr>
<td align="right">39</td>
<td><a href="/wiki/Legnica" title="Legnica">Legnica</a></td>
<td><a href="/wiki/Lower_Silesian_Voivodeship" title="Lower Silesian Voivodeship">Lower Silesia</a></td>
<td align="right">107,100</td>
<td align="right">106,143
</td></tr>
<tr>
<td align="right">40</td>
<td><a href="/wiki/S%C5%82upsk" title="Słupsk">Słupsk</a></td>
<td><a href="/wiki/Pomeranian_Voivodeship" title="Pomeranian Voivodeship">Pomerania</a></td>
<td align="right">100,376</td>
<td align="right">99,827
</td></tr>
<tr>
<td align="right">41</td>
<td><a href="/wiki/Grudzi%C4%85dz" title="Grudziądz">Grudziądz</a></td>
<td><a href="/wiki/Kuyavian-Pomeranian_Voivodeship" title="Kuyavian-Pomeranian Voivodeship">Kuyavia-Pomerania</a></td>
<td align="right">99,943</td>
<td align="right">98,757
</td></tr>
<tr>
<td align="right">42</td>
<td><a href="/wiki/Jaworzno" title="Jaworzno">Jaworzno</a></td>
<td><a href="/wiki/Silesian_Voivodeship" title="Silesian Voivodeship">Silesia</a></td>
<td align="right">98,780</td>
<td align="right">96,600
</td></tr>
</tbody></table>
<h2><span class="mw-headline" id="Related_pages">Related pages</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Poland&amp;veaction=edit&amp;section=13" class="mw-editsection-visualeditor" title="Change section: Related pages">change</a><span class="mw-editsection-divider"> | </span><a href="/w/index.php?title=Poland&amp;action=edit&amp;section=13" title="Change section: Related pages">change source</a><span class="mw-editsection-bracket">]</span></span></h2>
<ul><li><a href="/wiki/List_of_rivers_of_Poland" title="List of rivers of Poland">List of rivers of Poland</a></li>
<li><a href="/wiki/Poland_at_the_Olympics" title="Poland at the Olympics">Poland at the Olympics</a></li>
<li><a href="/wiki/Poland_national_football_team" title="Poland national football team">Poland national football team</a></li></ul>
<h2><span class="mw-headline" id="References">References</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Poland&amp;veaction=edit&amp;section=14" class="mw-editsection-visualeditor" title="Change section: References">change</a><span class="mw-editsection-divider"> | </span><a href="/w/index.php?title=Poland&amp;action=edit&amp;section=14" title="Change section: References">change source</a><span class="mw-editsection-bracket">]</span></span></h2>
<style data-mw-deduplicate="TemplateStyles:r8087918">.mw-parser-output .reflist{font-size:90%;margin-bottom:0.5em;list-style-type:decimal}.mw-parser-output .reflist .references{font-size:100%;margin-bottom:0;list-style-type:inherit}.mw-parser-output .reflist-columns-2{column-width:30em}.mw-parser-output .reflist-columns-3{column-width:25em}.mw-parser-output .reflist-columns{margin-top:0.3em}.mw-parser-output .reflist-columns ol{margin-top:0}.mw-parser-output .reflist-columns li{page-break-inside:avoid;break-inside:avoid-column}.mw-parser-output .reflist-upper-alpha{list-style-type:upper-alpha}.mw-parser-output .reflist-upper-roman{list-style-type:upper-roman}.mw-parser-output .reflist-lower-alpha{list-style-type:lower-alpha}.mw-parser-output .reflist-lower-greek{list-style-type:lower-greek}.mw-parser-output .reflist-lower-roman{list-style-type:lower-roman}</style><div class="reflist">
<div class="mw-references-wrap mw-references-columns"><ol class="references">
<li id="cite_note-1"><span class="mw-cite-backlink"><a href="#cite_ref-1" aria-label="Jump up" title="Jump up">↑</a></span> <span class="reference-text"><style data-mw-deduplicate="TemplateStyles:r7983297">.mw-parser-output cite.citation{font-style:inherit;word-wrap:break-word}.mw-parser-output .citation q{quotes:"\"""\"""'""'"}.mw-parser-output .citation:target{background-color:rgba(0,127,255,0.133)}.mw-parser-output .id-lock-free a,.mw-parser-output .citation .cs1-lock-free a{background:linear-gradient(transparent,transparent),url("//upload.wikimedia.org/wikipedia/commons/6/65/Lock-green.svg")right 0.1em center/9px no-repeat}.mw-parser-output .id-lock-limited a,.mw-parser-output .id-lock-registration a,.mw-parser-output .citation .cs1-lock-limited a,.mw-parser-output .citation .cs1-lock-registration a{background:linear-gradient(transparent,transparent),url("//upload.wikimedia.org/wikipedia/commons/d/d6/Lock-gray-alt-2.svg")right 0.1em center/9px no-repeat}.mw-parser-output .id-lock-subscription a,.mw-parser-output .citation .cs1-lock-subscription a{background:linear-gradient(transparent,transparent),url("//upload.wikimedia.org/wikipedia/commons/a/aa/Lock-red-alt-2.svg")right 0.1em center/9px no-repeat}.mw-parser-output .cs1-ws-icon a{background:linear-gradient(transparent,transparent),url("//upload.wikimedia.org/wikipedia/commons/4/4c/Wikisource-logo.svg")right 0.1em center/12px no-repeat}.mw-parser-output .cs1-code{color:inherit;background:inherit;border:none;padding:inherit}.mw-parser-output .cs1-hidden-error{display:none;color:#d33}.mw-parser-output .cs1-visible-error{color:#d33}.mw-parser-output .cs1-maint{display:none;color:#3a3;margin-left:0.3em}.mw-parser-output .cs1-format{font-size:95%}.mw-parser-output .cs1-kern-left{padding-left:0.2em}.mw-parser-output .cs1-kern-right{padding-right:0.2em}.mw-parser-output .citation .mw-selflink{font-weight:inherit}</style><cite class="citation web cs1 cs1-prop-foreign-lang-source"><a rel="nofollow" class="external text" href="https://web.archive.org/web/20130116214520/http://www.stat.gov.pl/cps/rde/xbcr/gus/PUBL_lu_nps2011_wyniki_nsp2011_22032012.pdf">"Wyniki Narodowego Spisu Powszechnego Ludności i Mieszkań 2011"</a> [Results of the National Census of Population and Housing 2011] <span class="cs1-format">(PDF)</span>. <i>Central Statistical Office</i> (in Polish). March 2012. Archived from <a rel="nofollow" class="external text" href="http://stat.gov.pl/cps/rde/xbcr/gus/lu_nps2011_wyniki_nsp2011_22032012.pdf">the original</a> <span class="cs1-format">(PDF)</span> on 16 January 2013.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Central+Statistical+Office&amp;rft.atitle=Wyniki+Narodowego+Spisu+Powszechnego+Ludno%C5%9Bci+i+Mieszka%C5%84+2011&amp;rft.date=2012-03&amp;rft_id=http%3A%2F%2Fstat.gov.pl%2Fcps%2Frde%2Fxbcr%2Fgus%2Flu_nps2011_wyniki_nsp2011_22032012.pdf&amp;rfr_id=info%3Asid%2Fsimple.wikipedia.org%3APoland" class="Z3988"></span></span>
</li>
<li id="cite_note-2"><span class="mw-cite-backlink"><a href="#cite_ref-2" aria-label="Jump up" title="Jump up">↑</a></span> <span class="reference-text"><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r7983297"><cite class="citation web cs1"><a rel="nofollow" class="external text" href="https://www.indexmundi.com/poland/demographics_profile.html">"Poland Demographics Profile"</a>. <a rel="nofollow" class="external text" href="https://web.archive.org/web/20200704005122/https://www.indexmundi.com/poland/demographics_profile.html">Archived</a> from the original on 2020-07-04<span class="reference-accessdate">. Retrieved <span class="nowrap">2020-05-21</span></span>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=unknown&amp;rft.btitle=Poland+Demographics+Profile&amp;rft_id=https%3A%2F%2Fwww.indexmundi.com%2Fpoland%2Fdemographics_profile.html&amp;rfr_id=info%3Asid%2Fsimple.wikipedia.org%3APoland" class="Z3988"></span></span>
</li>
<li id="cite_note-imf-gdp-3"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-imf-gdp_3-0"><span class="cite-accessibility-label">Jump up to: </span>3.0</a></sup> <sup><a href="#cite_ref-imf-gdp_3-1">3.1</a></sup></span> <span class="reference-text"><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r7983297"><cite class="citation web cs1"><a rel="nofollow" class="external text" href="http://www.imf.org/external/pubs/ft/weo/2017/02/weodata/weorept.aspx?pr.x=94&amp;pr.y=3&amp;sy=2017&amp;ey=2017&amp;scsm=1&amp;ssd=1&amp;sort=country&amp;ds=.&amp;br=1&amp;c=964&amp;s=NGDPD%2CNGDPDPC%2CPPPGDP%2CPPPPC&amp;grp=0&amp;a=">"5. Report for Selected Countries and Subjects"</a>. <a href="/wiki/International_Monetary_Fund" title="International Monetary Fund">International Monetary Fund</a>. <a rel="nofollow" class="external text" href="https://web.archive.org/web/20200524063453/https://www.imf.org/external/pubs/ft/weo/2017/02/weodata/weorept.aspx?pr.x=94&amp;pr.y=3&amp;sy=2017&amp;ey=2017&amp;scsm=1&amp;ssd=1&amp;sort=country&amp;ds=.&amp;br=1&amp;c=964&amp;s=NGDPD%2CNGDPDPC%2CPPPGDP%2CPPPPC&amp;grp=0&amp;a=">Archived</a> from the original on 24 May 2020<span class="reference-accessdate">. Retrieved <span class="nowrap">8 May</span> 2017</span>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=unknown&amp;rft.btitle=5.+Report+for+Selected+Countries+and+Subjects&amp;rft.pub=International+Monetary+Fund&amp;rft_id=http%3A%2F%2Fwww.imf.org%2Fexternal%2Fpubs%2Fft%2Fweo%2F2017%2F02%2Fweodata%2Fweorept.aspx%3Fpr.x%3D94%26pr.y%3D3%26sy%3D2017%26ey%3D2017%26scsm%3D1%26ssd%3D1%26sort%3Dcountry%26ds%3D.%26br%3D1%26c%3D964%26s%3DNGDPD%252CNGDPDPC%252CPPPGDP%252CPPPPC%26grp%3D0%26a%3D&amp;rfr_id=info%3Asid%2Fsimple.wikipedia.org%3APoland" class="Z3988"></span></span>
</li>
<li id="cite_note-4"><span class="mw-cite-backlink"><a href="#cite_ref-4" aria-label="Jump up" title="Jump up">↑</a></span> <span class="reference-text"><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r7983297"><cite class="citation journal cs1"><a rel="nofollow" class="external text" href="https://fred.stlouisfed.org/series/SIPOVGINIPOL">"GINI Index for Poland"</a>. 17 October 2016. <a rel="nofollow" class="external text" href="https://web.archive.org/web/20170426055727/https://fred.stlouisfed.org/series/SIPOVGINIPOL">Archived</a> from the original on 26 April 2017<span class="reference-accessdate">. Retrieved <span class="nowrap">25 April</span> 2017</span>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=article&amp;rft.atitle=GINI+Index+for+Poland&amp;rft.date=2016-10-17&amp;rft_id=https%3A%2F%2Ffred.stlouisfed.org%2Fseries%2FSIPOVGINIPOL&amp;rfr_id=info%3Asid%2Fsimple.wikipedia.org%3APoland" class="Z3988"></span> <span class="cs1-hidden-error citation-comment"><code class="cs1-code">{{<a href="/wiki/Template:Cite_journal" title="Template:Cite journal">cite journal</a>}}</code>: </span><span class="cs1-hidden-error citation-comment">Cite journal requires <code class="cs1-code">|journal=</code> (<a href="/wiki/Help:CS1_errors#missing_periodical" title="Help:CS1 errors">help</a>)</span></span>
</li>
<li id="cite_note-HDI-5"><span class="mw-cite-backlink"><a href="#cite_ref-HDI_5-0" aria-label="Jump up" title="Jump up">↑</a></span> <span class="reference-text"><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r7983297"><cite class="citation web cs1"><a rel="nofollow" class="external text" href="http://hdr.undp.org/sites/default/files/hdr_2015_statistical_annex.pdf">"2015 Human Development Report"</a> <span class="cs1-format">(PDF)</span>. United Nations Development Programme. 2015. <a rel="nofollow" class="external text" href="https://web.archive.org/web/20200501154015/http://hdr.undp.org/sites/default/files/hdr_2015_statistical_annex.pdf">Archived</a> <span class="cs1-format">(PDF)</span> from the original on 1 May 2020<span class="reference-accessdate">. Retrieved <span class="nowrap">14 December</span> 2015</span>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=unknown&amp;rft.btitle=2015+Human+Development+Report&amp;rft.pub=United+Nations+Development+Programme&amp;rft.date=2015&amp;rft_id=http%3A%2F%2Fhdr.undp.org%2Fsites%2Fdefault%2Ffiles%2Fhdr_2015_statistical_annex.pdf&amp;rfr_id=info%3Asid%2Fsimple.wikipedia.org%3APoland" class="Z3988"></span></span>
</li>
<li id="cite_note-CSO_2008-6"><span class="mw-cite-backlink"><a href="#cite_ref-CSO_2008_6-0" aria-label="Jump up" title="Jump up">↑</a></span> <span class="reference-text"><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r7983297"><cite class="citation web cs1"><a rel="nofollow" class="external text" href="http://www.stat.gov.pl/cps/rde/xbcr/gus/PUBL_maly_rocznik_statystyczny_2008.pdf">"Concise Statistical Yearbook of Poland, 2008"</a> <span class="cs1-format">(PDF)</span>. <a href="/w/index.php?title=Central_Statistical_Office_(Poland)&amp;action=edit&amp;redlink=1" class="new" title="Central Statistical Office (Poland) (not yet started)">Central Statistical Office (Poland)</a>. 28 July 2008. <a rel="nofollow" class="external text" href="https://web.archive.org/web/20081028221046/http://www.stat.gov.pl/cps/rde/xbcr/gus/PUBL_maly_rocznik_statystyczny_2008.pdf">Archived</a> <span class="cs1-format">(PDF)</span> from the original on 2008-10-28<span class="reference-accessdate">. Retrieved <span class="nowrap">2008-08-12</span></span>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=unknown&amp;rft.btitle=Concise+Statistical+Yearbook+of+Poland%2C+2008&amp;rft.pub=Central+Statistical+Office+%28Poland%29&amp;rft.date=2008-07-28&amp;rft_id=http%3A%2F%2Fwww.stat.gov.pl%2Fcps%2Frde%2Fxbcr%2Fgus%2FPUBL_maly_rocznik_statystyczny_2008.pdf&amp;rfr_id=info%3Asid%2Fsimple.wikipedia.org%3APoland" class="Z3988"></span></span>
</li>
<li id="cite_note-7"><span class="mw-cite-backlink"><a href="#cite_ref-7" aria-label="Jump up" title="Jump up">↑</a></span> <span class="reference-text"><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r7983297"><cite id="CITEREFSmith1996" class="citation book cs1">Smith, Christian (1996). <a rel="nofollow" class="external text" href="https://books.google.com/books?id=39SoSG4NGAoC&amp;dq=poland%27s+millennium&amp;pg=PA77"><i>Disruptive Religion: The Force of Faith in Social-movement Activism</i></a>. <a href="/wiki/ISBN_(identifier)" class="mw-redirect" title="ISBN (identifier)">ISBN</a>&nbsp;<a href="/wiki/Special:BookSources/9780415914055" title="Special:BookSources/9780415914055"><bdi>9780415914055</bdi></a>. <a rel="nofollow" class="external text" href="https://web.archive.org/web/20210411233507/https://books.google.com/books?id=39SoSG4NGAoC&amp;pg=PA77&amp;lpg=PA77&amp;dq=poland%27s+millennium&amp;sig=uQ-qK9oxqMuHmVvZJj8lszrm1">Archived</a> from the original on 11 April 2021<span class="reference-accessdate">. Retrieved <span class="nowrap">9 September</span> 2013</span>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=book&amp;rft.btitle=Disruptive+Religion%3A+The+Force+of+Faith+in+Social-movement+Activism&amp;rft.date=1996&amp;rft.isbn=9780415914055&amp;rft.aulast=Smith&amp;rft.aufirst=Christian&amp;rft_id=https%3A%2F%2Fbooks.google.com%2Fbooks%3Fid%3D39SoSG4NGAoC%26dq%3Dpoland%2527s%2Bmillennium%26pg%3DPA77&amp;rfr_id=info%3Asid%2Fsimple.wikipedia.org%3APoland" class="Z3988"></span></span>
</li>
<li id="cite_note-unee-8"><span class="mw-cite-backlink"><a href="#cite_ref-unee_8-0" aria-label="Jump up" title="Jump up">↑</a></span> <span class="reference-text"><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r7983297"><cite id="CITEREFUN_Statistics_Division2010" class="citation web cs1">UN Statistics Division (1 April 2010). <a rel="nofollow" class="external text" href="http://unstats.un.org/unsd/methods/m49/m49regin.htm#europe">"Standard Country and Area Codes Classifications (M49)"</a>. United Nations Organization. <a rel="nofollow" class="external text" href="https://web.archive.org/web/20181226004109/https://unstats.un.org/unsd/methods/m49/m49regin.htm#europe">Archived</a> from the original on 26 December 2018<span class="reference-accessdate">. Retrieved <span class="nowrap">17 April</span> 2014</span>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=unknown&amp;rft.btitle=Standard+Country+and+Area+Codes+Classifications+%28M49%29&amp;rft.pub=United+Nations+Organization&amp;rft.date=2010-04-01&amp;rft.au=UN+Statistics+Division&amp;rft_id=http%3A%2F%2Funstats.un.org%2Funsd%2Fmethods%2Fm49%2Fm49regin.htm%23europe&amp;rfr_id=info%3Asid%2Fsimple.wikipedia.org%3APoland" class="Z3988"></span></span>
</li>
<li id="cite_note-CIAWFBook-9"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-CIAWFBook_9-0"><span class="cite-accessibility-label">Jump up to: </span>9.0</a></sup> <sup><a href="#cite_ref-CIAWFBook_9-1">9.1</a></sup></span> <span class="reference-text"><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r7983297"><cite class="citation web cs1"><a rel="nofollow" class="external text" href="https://www.cia.gov/library/publications/the-world-factbook/geos/pl.html">"Poland"</a>. <i><a href="/wiki/The_World_Factbook" title="The World Factbook">The World Factbook</a></i>. <a href="/wiki/Central_Intelligence_Agency" title="Central Intelligence Agency">Central Intelligence Agency</a>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=The+World+Factbook&amp;rft.atitle=Poland&amp;rft_id=https%3A%2F%2Fwww.cia.gov%2Flibrary%2Fpublications%2Fthe-world-factbook%2Fgeos%2Fpl.html&amp;rfr_id=info%3Asid%2Fsimple.wikipedia.org%3APoland" class="Z3988"></span></span>
</li>
<li id="cite_note-REF03-10"><span class="mw-cite-backlink">↑ <sup><a href="#cite_ref-REF03_10-0"><span class="cite-accessibility-label">Jump up to: </span>10.0</a></sup> <sup><a href="#cite_ref-REF03_10-1">10.1</a></sup></span> <span class="reference-text">Teeple, J. B. (2002). <i>Timelines of World History</i>. Publisher: DK Adult.</span>
</li>
<li id="cite_note-11"><span class="mw-cite-backlink"><a href="#cite_ref-11" aria-label="Jump up" title="Jump up">↑</a></span> <span class="reference-text"><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r7983297"><cite id="CITEREFBurant1985" class="citation journal cs1">Burant, Stephen R. (April 1, 1985). <a rel="nofollow" class="external text" href="https://journals.sagepub.com/doi/abs/10.1177/026569148501500201?journalCode=ehqb">"The January Uprising of 1863 in Poland: Sources of Disaffection and the Arenas of Revolt"</a>. <i>European History Quarterly</i>. Sage Journals. <b>15</b> (2): 131–56. <a href="/wiki/Doi_(identifier)" class="mw-redirect" title="Doi (identifier)">doi</a>:<a rel="nofollow" class="external text" href="https://doi.org/10.1177%2F026569148501500201">10.1177/026569148501500201</a>. <a href="/wiki/S2CID_(identifier)" class="mw-redirect" title="S2CID (identifier)">S2CID</a>&nbsp;<a rel="nofollow" class="external text" href="https://api.semanticscholar.org/CorpusID:143799338">143799338</a>. <a rel="nofollow" class="external text" href="https://web.archive.org/web/20210521133744/https://journals.sagepub.com/doi/abs/10.1177/026569148501500201?journalCode=ehqb&amp;">Archived</a> from the original on May 21, 2021<span class="reference-accessdate">. Retrieved <span class="nowrap">July 20,</span> 2020</span>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=article&amp;rft.jtitle=European+History+Quarterly&amp;rft.atitle=The+January+Uprising+of+1863+in+Poland%3A+Sources+of+Disaffection+and+the+Arenas+of+Revolt&amp;rft.volume=15&amp;rft.issue=2&amp;rft.pages=131-56&amp;rft.date=1985-04-01&amp;rft_id=info%3Adoi%2F10.1177%2F026569148501500201&amp;rft_id=https%3A%2F%2Fapi.semanticscholar.org%2FCorpusID%3A143799338%23id-name%3DS2CID&amp;rft.aulast=Burant&amp;rft.aufirst=Stephen+R.&amp;rft_id=https%3A%2F%2Fjournals.sagepub.com%2Fdoi%2Fabs%2F10.1177%2F026569148501500201%3FjournalCode%3Dehqb&amp;rfr_id=info%3Asid%2Fsimple.wikipedia.org%3APoland" class="Z3988"></span></span>
</li>
<li id="cite_note-12"><span class="mw-cite-backlink"><a href="#cite_ref-12" aria-label="Jump up" title="Jump up">↑</a></span> <span class="reference-text">In first version of that line western <a href="/wiki/Ukraine" title="Ukraine">Ukraine</a> with <a href="/wiki/Lviv" title="Lviv">Lviv</a> may come to Poland</span>
</li>
</ol></div></div>
<h2><span class="mw-headline" id="Other_websites">Other websites</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Poland&amp;veaction=edit&amp;section=15" class="mw-editsection-visualeditor" title="Change section: Other websites">change</a><span class="mw-editsection-divider"> | </span><a href="/w/index.php?title=Poland&amp;action=edit&amp;section=15" title="Change section: Other websites">change source</a><span class="mw-editsection-bracket">]</span></span></h2>
<table class="metadata plainlinks mbox-small" style="padding:0.25em 0.5em 0.5em 0.75em;border:1px solid #aaa;background:#f9f9f9;">

<tbody><tr>
<td colspan="2" style="padding-bottom:0.75em;border-bottom:1px solid #aaa;text-align:center;"><div style="clear:both;">Find more about<br><b>Poland</b><br>at Wikipedia's <a href="/wiki/Wikipedia:Sister_projects" title="Wikipedia:Sister projects">sister projects</a> </div>
</td></tr>
<tr style="height:25px;">
<td style="padding-top:0.75em;"><a href="https://simple.wiktionary.org/wiki/Special:Search/Poland" title="Search Wiktionary"><img alt="Search Wiktionary" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Wiktionary-logo-en.svg/23px-Wiktionary-logo-en.svg.png" decoding="async" width="23" height="25" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Wiktionary-logo-en.svg/35px-Wiktionary-logo-en.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Wiktionary-logo-en.svg/46px-Wiktionary-logo-en.svg.png 2x" data-file-width="1000" data-file-height="1089"></a>
</td>
<td style="padding-top:0.75em;"><a href="https://simple.wiktionary.org/wiki/Special:Search/Poland" class="extiw" title="wikt:Special:Search/Poland">Definitions</a> from Wiktionary
</td></tr>
<tr style="height:25px;">
<td><a href="https://commons.wikimedia.org/wiki/Special:Search/Poland" title="Search Commons"><img alt="Search Commons" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Commons-logo.svg/18px-Commons-logo.svg.png" decoding="async" width="18" height="25" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Commons-logo.svg/28px-Commons-logo.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Commons-logo.svg/37px-Commons-logo.svg.png 2x" data-file-width="1024" data-file-height="1376"></a>
</td>
<td><a href="https://commons.wikimedia.org/wiki/Special:Search/Poland" class="extiw" title="commons:Special:Search/Poland">Media</a> from Commons
</td></tr>
<tr style="height:25px;">
<td><a href="https://en.wikinews.org/wiki/Special:Search/Poland" title="Search Wikinews"><img alt="Search Wikinews" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/24/Wikinews-logo.svg/25px-Wikinews-logo.svg.png" decoding="async" width="25" height="14" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/24/Wikinews-logo.svg/38px-Wikinews-logo.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/24/Wikinews-logo.svg/50px-Wikinews-logo.svg.png 2x" data-file-width="759" data-file-height="415"></a>
</td>
<td><a href="https://en.wikinews.org/wiki/Special:Search/Poland" class="extiw" title="wikinews:Special:Search/Poland">News stories</a> from Wikinews
</td></tr>
<tr style="height:25px;">
<td><a href="https://en.wikiquote.org/wiki/Special:Search/Poland" title="Search Wikiquote"><img alt="Search Wikiquote" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Wikiquote-logo.svg/21px-Wikiquote-logo.svg.png" decoding="async" width="21" height="25" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Wikiquote-logo.svg/32px-Wikiquote-logo.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Wikiquote-logo.svg/42px-Wikiquote-logo.svg.png 2x" data-file-width="300" data-file-height="355"></a>
</td>
<td><a href="https://en.wikiquote.org/wiki/Special:Search/Poland" class="extiw" title="wikiquote:Special:Search/Poland">Quotations</a> from Wikiquote
</td></tr>
<tr style="height:25px;">
<td><a href="https://en.wikisource.org/wiki/Special:Search/Poland" title="Search Wikisource"><img alt="Search Wikisource" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Wikisource-logo.svg/24px-Wikisource-logo.svg.png" decoding="async" width="24" height="25" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Wikisource-logo.svg/36px-Wikisource-logo.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Wikisource-logo.svg/48px-Wikisource-logo.svg.png 2x" data-file-width="410" data-file-height="430"></a>
</td>
<td><a href="https://en.wikisource.org/wiki/Special:Search/Poland" class="extiw" title="wikisource:Special:Search/Poland">Source texts</a> from Wikisource
</td></tr>
<tr style="height:25px;">
<td><a href="https://en.wikibooks.org/wiki/Special:Search/Poland" title="Search Wikibooks"><img alt="Search Wikibooks" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Wikibooks-logo.svg/25px-Wikibooks-logo.svg.png" decoding="async" width="25" height="25" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Wikibooks-logo.svg/38px-Wikibooks-logo.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Wikibooks-logo.svg/50px-Wikibooks-logo.svg.png 2x" data-file-width="300" data-file-height="300"></a>
</td>
<td><a href="https://en.wikibooks.org/wiki/Special:Search/Poland" class="extiw" title="wikibooks:Special:Search/Poland">Textbooks</a> from Wikibooks
</td></tr>


<tr style="height:25px;">
<td><a href="https://en.wikiversity.org/wiki/Special:Search/Poland" title="Search Wikiversity"><img alt="Search Wikiversity" src="//upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Wikiversity-logo-en.svg/25px-Wikiversity-logo-en.svg.png" decoding="async" width="25" height="23" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Wikiversity-logo-en.svg/38px-Wikiversity-logo-en.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Wikiversity-logo-en.svg/50px-Wikiversity-logo-en.svg.png 2x" data-file-width="1000" data-file-height="900"></a>
</td>
<td><a href="https://en.wikiversity.org/wiki/Special:Search/Poland" class="extiw" title="wikiversity:Special:Search/Poland">Learning resources</a> from Wikiversity
</td></tr>









</tbody></table>
<ul><li><a rel="nofollow" class="external text" href="http://www.pot.gov.pl:80/potgov_front_page">Tourist information portal</a></li>
<li><a rel="nofollow" class="external text" href="http://www.poland.gov.pl/">Poland.gov.pl - Polish national portal</a> <a rel="nofollow" class="external text" href="https://web.archive.org/web/20081029120855/http://www.poland.gov.pl/">Archived</a> 2008-10-29 at the <a href="/wiki/Wayback_Machine" title="Wayback Machine">Wayback Machine</a></li>
<li><a rel="nofollow" class="external text" href="http://www.msz.gov.pl/">Ministry of Foreign Affairs</a></li>
<li><a rel="nofollow" class="external text" href="https://www.cia.gov/library/publications/the-world-factbook/geos/pl.html">Poland at the World Factbook</a> <a rel="nofollow" class="external text" href="https://web.archive.org/web/20190818041414/https://www.cia.gov/library/publications/the-world-factbook/geos/pl.html">Archived</a> 2019-08-18 at the <a href="/wiki/Wayback_Machine" title="Wayback Machine">Wayback Machine</a></li>
<li><a rel="nofollow" class="external text" href="http://www.state.gov/r/pa/ei/bgn/2875.htm">Background Note: Poland</a></li>
<li><a rel="nofollow" class="external text" href="http://wiki.worldflicks.org/poland.html">WorldFlicks in Poland: photos and interesting places on Google Maps</a> <a rel="nofollow" class="external text" href="https://web.archive.org/web/20080503024828/http://wiki.worldflicks.org/poland.html">Archived</a> 2008-05-03 at the <a href="/wiki/Wayback_Machine" title="Wayback Machine">Wayback Machine</a></li></ul>
<div class="navbox-styles nomobile"><style data-mw-deduplicate="TemplateStyles:r8034727">.mw-parser-output .navbox{box-sizing:border-box;border:1px solid #a2a9b1;width:100%;clear:both;font-size:88%;text-align:center;padding:1px;margin:1em auto 0}.mw-parser-output .navbox .navbox{margin-top:0}.mw-parser-output .navbox+.navbox,.mw-parser-output .navbox+.navbox-styles+.navbox{margin-top:-1px}.mw-parser-output .navbox-inner,.mw-parser-output .navbox-subgroup{width:100%}.mw-parser-output .navbox-group,.mw-parser-output .navbox-title,.mw-parser-output .navbox-abovebelow{padding:0.25em 1em;line-height:1.5em;text-align:center}.mw-parser-output .navbox-group{white-space:nowrap;text-align:right}.mw-parser-output .navbox,.mw-parser-output .navbox-subgroup{background-color:#fdfdfd}.mw-parser-output .navbox-list{line-height:1.5em;border-color:#fdfdfd}.mw-parser-output .navbox-list-with-group{text-align:left;border-left-width:2px;border-left-style:solid}.mw-parser-output tr+tr>.navbox-abovebelow,.mw-parser-output tr+tr>.navbox-group,.mw-parser-output tr+tr>.navbox-image,.mw-parser-output tr+tr>.navbox-list{border-top:2px solid #fdfdfd}.mw-parser-output .navbox-title{background-color:#ccf}.mw-parser-output .navbox-abovebelow,.mw-parser-output .navbox-group,.mw-parser-output .navbox-subgroup .navbox-title{background-color:#ddf}.mw-parser-output .navbox-subgroup .navbox-group,.mw-parser-output .navbox-subgroup .navbox-abovebelow{background-color:#e6e6ff}.mw-parser-output .navbox-even{background-color:#f7f7f7}.mw-parser-output .navbox-odd{background-color:transparent}.mw-parser-output .navbox .hlist td dl,.mw-parser-output .navbox .hlist td ol,.mw-parser-output .navbox .hlist td ul,.mw-parser-output .navbox td.hlist dl,.mw-parser-output .navbox td.hlist ol,.mw-parser-output .navbox td.hlist ul{padding:0.125em 0}.mw-parser-output .navbox .navbar{display:block;font-size:100%}.mw-parser-output .navbox-title .navbar{float:left;text-align:left;margin-right:0.5em}</style></div><div role="navigation" class="navbox" aria-labelledby="23px&amp;#124;border_&amp;#124;alt=&amp;#124;link=_Countries_and_territories_of_Europe" style="padding:3px"><table class="nowraplinks mw-collapsible autocollapse navbox-inner mw-made-collapsible mw-collapsed" style="border-spacing:0;background:transparent;color:inherit"><tbody><tr><th scope="col" class="navbox-title" colspan="2"><span class="mw-collapsible-toggle mw-collapsible-toggle-default mw-collapsible-toggle-collapsed" role="button" tabindex="0" aria-expanded="false"><a class="mw-collapsible-text">Expand</a></span><style data-mw-deduplicate="TemplateStyles:r7983369">.mw-parser-output .navbar{display:inline;font-size:88%;font-weight:normal}.mw-parser-output .navbar-collapse{float:left;text-align:left}.mw-parser-output .navbar-boxtext{word-spacing:0}.mw-parser-output .navbar ul{display:inline-block;white-space:nowrap;line-height:inherit}.mw-parser-output .navbar-brackets::before{margin-right:-0.125em;content:"[ "}.mw-parser-output .navbar-brackets::after{margin-left:-0.125em;content:" ]"}.mw-parser-output .navbar li{word-spacing:-0.125em}.mw-parser-output .navbar a>span,.mw-parser-output .navbar a>abbr{text-decoration:inherit}.mw-parser-output .navbar-mini abbr{font-variant:small-caps;border-bottom:none;text-decoration:none;cursor:inherit}.mw-parser-output .navbar-ct-full{font-size:114%;margin:0 7em}.mw-parser-output .navbar-ct-mini{font-size:114%;margin:0 4em}</style><div class="navbar plainlinks hlist navbar-mini"><ul><li class="nv-view"><a href="/wiki/Template:Europe" title="Template:Europe"><abbr title="View this template" style=";;background:none transparent;border:none;box-shadow:none;padding:0;">v</abbr></a></li><li class="nv-talk"><a href="/wiki/Template_talk:Europe" title="Template talk:Europe"><abbr title="Discuss this template" style=";;background:none transparent;border:none;box-shadow:none;padding:0;">t</abbr></a></li><li class="nv-edit"><a class="external text" href="https://simple.wikipedia.org/w/index.php?title=Template:Europe&amp;action=edit"><abbr title="Edit this template" style=";;background:none transparent;border:none;box-shadow:none;padding:0;">e</abbr></a></li></ul></div><div id="23px&amp;#124;border_&amp;#124;alt=&amp;#124;link=_Countries_and_territories_of_Europe" style="font-size:114%;margin:0 4em"><span class="flagicon"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Flag_of_Europe.svg/23px-Flag_of_Europe.svg.png" decoding="async" width="23" height="15" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Flag_of_Europe.svg/35px-Flag_of_Europe.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Flag_of_Europe.svg/46px-Flag_of_Europe.svg.png 2x" data-file-width="810" data-file-height="540"></span> <a href="/wiki/Country" title="Country">Countries</a> and territories of <a href="/wiki/Europe" title="Europe">Europe</a></div></th></tr><tr style="display: none;"><th scope="row" class="navbox-group" style="width:1%"><a href="/wiki/Country" title="Country">Countries</a></th><td class="navbox-list-with-group navbox-list navbox-odd" style="width:100%;padding:0"><div style="padding:0 0.25em"><a href="/wiki/Albania" title="Albania">Albania</a> – <a href="/wiki/Andorra" title="Andorra">Andorra</a>  – <a href="/wiki/Austria" title="Austria">Austria</a>  – <a href="/wiki/Belarus" title="Belarus">Belarus</a> – <a href="/wiki/Belgium" title="Belgium">Belgium</a> – <a href="/wiki/Bosnia_and_Herzegovina" title="Bosnia and Herzegovina">Bosnia and Herzegovina</a> – <a href="/wiki/Bulgaria" title="Bulgaria">Bulgaria</a> – <a href="/wiki/Croatia" title="Croatia">Croatia</a> – <a href="/wiki/Republic_of_Cyprus" title="Republic of Cyprus">Republic of Cyprus</a><sup>1</sup> – <a href="/wiki/Czech_Republic" title="Czech Republic">Czech Republic</a> – <a href="/wiki/Denmark" title="Denmark">Denmark</a><sup>2,4</sup> – <a href="/wiki/Estonia" title="Estonia">Estonia</a> – <a href="/wiki/Finland" title="Finland">Finland</a> – <a href="/wiki/France" title="France">France</a><sup>4</sup> – <a href="/wiki/Georgia_(country)" title="Georgia (country)">Georgia</a><sup>1</sup> – <a href="/wiki/Germany" title="Germany">Germany</a> – <a href="/wiki/Greece" title="Greece">Greece</a> – <a href="/wiki/Hungary" title="Hungary">Hungary</a> – <a href="/wiki/Iceland" title="Iceland">Iceland</a> – <a href="/wiki/Republic_of_Ireland" title="Republic of Ireland">Ireland</a> – <a href="/wiki/Italy" title="Italy">Italy</a>  – <a href="/wiki/Latvia" title="Latvia">Latvia</a> – <a href="/wiki/Liechtenstein" title="Liechtenstein">Liechtenstein</a> – <a href="/wiki/Lithuania" title="Lithuania">Lithuania</a> – <a href="/wiki/Luxembourg" title="Luxembourg">Luxembourg</a> – <a href="/wiki/Malta" title="Malta">Malta</a> – <a href="/wiki/Moldova" title="Moldova">Moldova</a> – <a href="/wiki/Monaco" title="Monaco">Monaco</a> – <a href="/wiki/Montenegro" title="Montenegro">Montenegro</a> – <a href="/wiki/Netherlands" title="Netherlands">Netherlands</a><sup>4</sup> – <a href="/wiki/North_Macedonia" title="North Macedonia">North Macedonia</a> – <a href="/wiki/Norway" title="Norway">Norway</a><sup>4</sup> – <a class="mw-selflink selflink">Poland</a> – <a href="/wiki/Portugal" title="Portugal">Portugal</a><sup>4,6</sup> – <a href="/wiki/Romania" title="Romania">Romania</a> – <a href="/wiki/Russia" title="Russia">Russia</a><sup>1</sup> – <a href="/wiki/San_Marino" title="San Marino">San Marino</a> – <a href="/wiki/Serbia" title="Serbia">Serbia</a> – <a href="/wiki/Slovakia" title="Slovakia">Slovakia</a> – <a href="/wiki/Slovenia" title="Slovenia">Slovenia</a> – <a href="/wiki/Spain" title="Spain">Spain</a><sup>4,6</sup> – <a href="/wiki/Sweden" title="Sweden">Sweden</a> – <a href="/wiki/Switzerland" title="Switzerland">Switzerland</a> – <a href="/wiki/Turkey" title="Turkey">Turkey</a><sup>1</sup> – <a href="/wiki/Ukraine" title="Ukraine">Ukraine</a> – <a href="/wiki/United_Kingdom" title="United Kingdom">United Kingdom</a><sup>4</sup> – <a href="/wiki/Vatican_City" title="Vatican City">Vatican City</a></div></td></tr><tr style="display: none;"><th scope="row" class="navbox-group" style="width:1%"><b><a href="/wiki/List_of_dependent_territories" class="mw-redirect" title="List of dependent territories">Dependencies</a></b></th><td class="navbox-list-with-group navbox-list navbox-even" style="width:100%;padding:0"><div style="padding:0 0.25em"><a href="/wiki/Akrotiri_and_Dhekelia" title="Akrotiri and Dhekelia">Akrotiri and Dhekelia</a><sup>1</sup> – <a href="/wiki/Azores" title="Azores">Azores</a><sup>5</sup> – <a href="/wiki/Ceuta" title="Ceuta">Ceuta</a><sup>5, 6</sup> – <a href="/wiki/Faroe_Islands" title="Faroe Islands">Faroe Islands</a><sup>5</sup> – <a href="/wiki/Gibraltar" title="Gibraltar">Gibraltar</a><sup>5</sup> – <a href="/wiki/Greenland" title="Greenland">Greenland</a><sup>5,2</sup> – <a href="/wiki/Guernsey" title="Guernsey">Guernsey</a> – <a href="/wiki/Jan_Mayen" title="Jan Mayen">Jan Mayen</a> – <a href="/wiki/Jersey" title="Jersey">Jersey</a> – <a href="/wiki/Isle_of_Man" title="Isle of Man">Isle of Man</a> – <a href="/wiki/Melilla" title="Melilla">Melilla</a><sup>5,6</sup> – <a href="/wiki/Svalbard" title="Svalbard">Svalbard</a></div></td></tr><tr style="display: none;"><th scope="row" class="navbox-group" style="width:1%"><b><a href="/wiki/List_of_unrecognized_countries" class="mw-redirect" title="List of unrecognized countries">Other Countries</a></b></th><td class="navbox-list-with-group navbox-list navbox-odd" style="width:100%;padding:0"><div style="padding:0 0.25em"><a href="/wiki/Abkhazia" title="Abkhazia">Abkhazia</a><sup>1,3</sup> – <a href="/wiki/Kosovo" title="Kosovo">Kosovo</a><sup>3</sup> – <a href="/wiki/South_Ossetia" title="South Ossetia">South Ossetia</a><sup>1, 3</sup> – <a href="/wiki/Transnistria" title="Transnistria">Transnistria</a> – <a href="/wiki/Turkish_Republic_of_Northern_Cyprus" class="mw-redirect" title="Turkish Republic of Northern Cyprus">Turkish Republic of Northern Cyprus</a><sup>1,3</sup></div></td></tr><tr style="display: none;"><td colspan="2" class="navbox-list navbox-even" style="width:100%;padding:0"><div style="padding:0 0.25em">1. <a href="/wiki/Transcontinental_country" title="Transcontinental country">Transcontinental country</a>/territory that is part of both Europe and Asia. 2. Territory or with territory geographically part of North America. 3. Partially recognized. 4. Not all dependent territories are listed. 5. Territory has some form of self-rule. 6.  Territory or with territory geographically part of Africa.</div></td></tr></tbody></table></div>
<div class="navbox-styles nomobile"><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r8034727"></div><div role="navigation" class="navbox" aria-labelledby="European_Union_member_and_candidate_countries" style="padding:3px"><table class="nowraplinks mw-collapsible autocollapse navbox-inner mw-made-collapsible mw-collapsed" style="border-spacing:0;background:transparent;color:inherit"><tbody><tr><th scope="col" class="navbox-title" colspan="3"><span class="mw-collapsible-toggle mw-collapsible-toggle-default mw-collapsible-toggle-collapsed" role="button" tabindex="0" aria-expanded="false"><a class="mw-collapsible-text">Expand</a></span><div id="European_Union_member_and_candidate_countries" style="font-size:114%;margin:0 4em"><a href="/wiki/European_Union" title="European Union">European Union</a> member and candidate countries</div></th></tr><tr style="display: none;"><th scope="row" class="navbox-group" style="width:1%">Current members</th><td class="navbox-list-with-group navbox-list navbox-odd" style="width:100%;padding:0"><div style="padding:0 0.25em"><a href="/wiki/Austria" title="Austria">Austria</a>&nbsp;<b>·</b>  <a href="/wiki/Belgium" title="Belgium">Belgium</a>&nbsp;<b>·</b>  <a href="/wiki/Bulgaria" title="Bulgaria">Bulgaria</a>&nbsp;<b>·</b>  <a href="/wiki/Croatia" title="Croatia">Croatia</a>&nbsp;<b>·</b>  <a href="/wiki/Cyprus" class="mw-redirect" title="Cyprus">Cyprus</a>&nbsp;<b>·</b>  <a href="/wiki/Czech_Republic" title="Czech Republic">Czech&nbsp;Republic</a>&nbsp;<b>·</b>  <a href="/wiki/Denmark" title="Denmark">Denmark</a>&nbsp;<b>·</b>  <a href="/wiki/Estonia" title="Estonia">Estonia</a>&nbsp;<b>·</b>  <a href="/wiki/Finland" title="Finland">Finland</a>&nbsp;<b>·</b>  <a href="/wiki/France" title="France">France</a>&nbsp;<b>·</b>  <a href="/wiki/Germany" title="Germany">Germany</a>&nbsp;<b>·</b>  <a href="/wiki/Greece" title="Greece">Greece</a>&nbsp;<b>·</b>  <a href="/wiki/Hungary" title="Hungary">Hungary</a>&nbsp;<b>·</b>  <a href="/wiki/Republic_of_Ireland" title="Republic of Ireland">Ireland</a>&nbsp;<b>·</b>  <a href="/wiki/Italy" title="Italy">Italy</a>&nbsp;<b>·</b>  <a href="/wiki/Latvia" title="Latvia">Latvia</a>&nbsp;<b>·</b>  <a href="/wiki/Lithuania" title="Lithuania">Lithuania</a>&nbsp;<b>·</b>  <a href="/wiki/Luxembourg" title="Luxembourg">Luxembourg</a>&nbsp;<b>·</b>  <a href="/wiki/Malta" title="Malta">Malta</a>&nbsp;<b>·</b>  <a href="/wiki/Netherlands" title="Netherlands">Netherlands</a>&nbsp;<b>·</b>  <a class="mw-selflink selflink">Poland</a>&nbsp;<b>·</b>  <a href="/wiki/Portugal" title="Portugal">Portugal</a>&nbsp;<b>·</b>  <a href="/wiki/Romania" title="Romania">Romania</a>&nbsp;<b>·</b>  <a href="/wiki/Slovakia" title="Slovakia">Slovakia</a>&nbsp;<b>·</b>  <a href="/wiki/Slovenia" title="Slovenia">Slovenia</a>&nbsp;<b>·</b>  <a href="/wiki/Spain" title="Spain">Spain</a>&nbsp;<b>·</b>  <a href="/wiki/Sweden" title="Sweden">Sweden</a></div></td><td class="noviewer navbox-image" rowspan="4" style="width:1px;padding:0 0 0 2px"><div><a href="/wiki/File:Flag_of_Europe.svg" class="image"><img alt="Flag of Europe.svg" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Flag_of_Europe.svg/65px-Flag_of_Europe.svg.png" decoding="async" width="65" height="43" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Flag_of_Europe.svg/98px-Flag_of_Europe.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Flag_of_Europe.svg/130px-Flag_of_Europe.svg.png 2x" data-file-width="810" data-file-height="540"></a></div></td></tr><tr style="display: none;"><th scope="row" class="navbox-group" style="width:1%">Candidates</th><td class="navbox-list-with-group navbox-list navbox-even" style="width:100%;padding:0"><div style="padding:0 0.25em"><a href="/wiki/Iceland" title="Iceland">Iceland</a>&nbsp;<b>·</b>  <a href="/wiki/Montenegro" title="Montenegro">Montenegro</a>&nbsp;<b>·</b>  <a href="/wiki/North_Macedonia" title="North Macedonia">North Macedonia</a>&nbsp;<b>·</b>  <a href="/wiki/Serbia" title="Serbia">Serbia</a>&nbsp;<b>·</b>  <a href="/wiki/Turkey" title="Turkey">Turkey</a></div></td></tr><tr style="display: none;"><th scope="row" class="navbox-group" style="width:1%">Potential candidates</th><td class="navbox-list-with-group navbox-list navbox-odd" style="width:100%;padding:0"><div style="padding:0 0.25em"><a href="/wiki/Albania" title="Albania">Albania</a>&nbsp;<b>·</b>  <a href="/wiki/Bosnia_and_Herzegovina" title="Bosnia and Herzegovina">Bosnia and Herzegovina</a>&nbsp;<b>·</b>  <a href="/wiki/Kosovo" title="Kosovo">Kosovo</a></div></td></tr><tr style="display: none;"><th scope="row" class="navbox-group" style="width:1%">Former members</th><td class="navbox-list-with-group navbox-list navbox-even" style="width:100%;padding:0"><div style="padding:0 0.25em"><a href="/wiki/United_Kingdom" title="United Kingdom">United Kingdom</a></div></td></tr><tr style="display: none;"><td class="navbox-abovebelow" colspan="3"><div><a href="/w/index.php?title=List_of_European_Union_member_states_by_accession&amp;action=edit&amp;redlink=1" class="new" title="List of European Union member states by accession (not yet started)">by accession</a>&nbsp;<b>·</b>  <a href="/w/index.php?title=List_of_European_Union_member_states_by_political_system&amp;action=edit&amp;redlink=1" class="new" title="List of European Union member states by political system (not yet started)">by political system</a>&nbsp;<b>·</b>  <a href="/wiki/List_of_European_Union_member_states_by_population" class="mw-redirect" title="List of European Union member states by population">by population</a>&nbsp;<b>·</b>  <a href="/w/index.php?title=Economy_of_the_European_Union&amp;action=edit&amp;redlink=1" class="new" title="Economy of the European Union (not yet started)">by GDP</a></div></td></tr></tbody></table></div>
<div class="navbox-styles nomobile"><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r8034727"></div><div role="navigation" class="navbox" aria-labelledby="North_Atlantic_Treaty_Organization_(NATO)" style="padding:3px"><table class="nowraplinks mw-collapsible autocollapse navbox-inner mw-made-collapsible mw-collapsed" style="border-spacing:0;background:transparent;color:inherit"><tbody><tr><th scope="col" class="navbox-title" colspan="2"><span class="mw-collapsible-toggle mw-collapsible-toggle-default mw-collapsible-toggle-collapsed" role="button" tabindex="0" aria-expanded="false"><a class="mw-collapsible-text">Expand</a></span><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r7983369"><div class="navbar plainlinks hlist navbar-mini"><ul><li class="nv-view"><a href="/wiki/Template:North_Atlantic_Treaty_Organization_(NATO)" title="Template:North Atlantic Treaty Organization (NATO)"><abbr title="View this template" style=";;background:none transparent;border:none;box-shadow:none;padding:0;">v</abbr></a></li><li class="nv-talk"><a href="/wiki/Template_talk:North_Atlantic_Treaty_Organization_(NATO)" title="Template talk:North Atlantic Treaty Organization (NATO)"><abbr title="Discuss this template" style=";;background:none transparent;border:none;box-shadow:none;padding:0;">t</abbr></a></li><li class="nv-edit"><a class="external text" href="https://simple.wikipedia.org/w/index.php?title=Template:North_Atlantic_Treaty_Organization_(NATO)&amp;action=edit"><abbr title="Edit this template" style=";;background:none transparent;border:none;box-shadow:none;padding:0;">e</abbr></a></li></ul></div><div id="North_Atlantic_Treaty_Organization_(NATO)" style="font-size:114%;margin:0 4em"><a href="/wiki/NATO" title="NATO">North Atlantic Treaty Organization (NATO)</a></div></th></tr><tr style="display: none;"><th scope="row" class="navbox-group" style="width:1%">Member countries</th><td class="navbox-list-with-group navbox-list navbox-odd" style="width:100%;padding:0"><div style="padding:0 0.25em"><a href="/wiki/Albania" title="Albania">Albania</a>&nbsp;<b>·</b>  <a href="/wiki/Belgium" title="Belgium">Belgium</a>&nbsp;<b>·</b>  <a href="/wiki/Bulgaria" title="Bulgaria">Bulgaria</a>&nbsp;<b>·</b>  <a href="/wiki/Canada" title="Canada">Canada</a>&nbsp;<b>·</b>  <a href="/wiki/Croatia" title="Croatia">Croatia</a>&nbsp;<b>·</b>  <a href="/wiki/Czech_Republic" title="Czech Republic">Czech Republic</a>&nbsp;<b>·</b>  <a href="/wiki/Denmark" title="Denmark">Denmark</a>&nbsp;<b>·</b>  <a href="/wiki/Estonia" title="Estonia">Estonia</a>&nbsp;<b>·</b>  <a href="/wiki/France" title="France">France</a>&nbsp;<b>·</b>  <a href="/wiki/Germany" title="Germany">Germany</a>&nbsp;<b>·</b>  <a href="/wiki/Greece" title="Greece">Greece</a>&nbsp;<b>·</b>  <a href="/wiki/Hungary" title="Hungary">Hungary</a>&nbsp;<b>·</b>  <a href="/wiki/Iceland" title="Iceland">Iceland</a>&nbsp;<b>·</b>  <a href="/wiki/Italy" title="Italy">Italy</a>&nbsp;<b>·</b>  <a href="/wiki/Latvia" title="Latvia">Latvia</a>&nbsp;<b>·</b>  <a href="/wiki/Lithuania" title="Lithuania">Lithuania</a>&nbsp;<b>·</b>  <a href="/wiki/Luxembourg" title="Luxembourg">Luxembourg</a>&nbsp;<b>·</b>  <a href="/wiki/Montenegro" title="Montenegro">Montenegro</a>&nbsp;<b>·</b>  <a href="/wiki/Netherlands" title="Netherlands">Netherlands</a>&nbsp;<b>·</b>  <a href="/wiki/North_Macedonia" title="North Macedonia">North Macedonia</a>&nbsp;<b>·</b>  <a href="/wiki/Norway" title="Norway">Norway</a>&nbsp;<b>·</b>  <a class="mw-selflink selflink">Poland</a>&nbsp;<b>·</b>  <a href="/wiki/Portugal" title="Portugal">Portugal</a>&nbsp;<b>·</b>  <a href="/wiki/Romania" title="Romania">Romania</a>&nbsp;<b>·</b>  <a href="/wiki/Slovakia" title="Slovakia">Slovakia</a>&nbsp;<b>·</b>  <a href="/wiki/Slovenia" title="Slovenia">Slovenia</a>&nbsp;<b>·</b>  <a href="/wiki/Spain" title="Spain">Spain</a>&nbsp;<b>·</b>  <a href="/wiki/Turkey" title="Turkey">Turkey</a>&nbsp;<b>·</b>  <a href="/wiki/United_Kingdom" title="United Kingdom">United Kingdom</a>&nbsp;<b>·</b>  <a href="/wiki/United_States" title="United States">United States</a></div></td></tr></tbody></table></div>
<div class="navbox-styles nomobile"><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r8034727"></div><div role="navigation" class="navbox authority-control" aria-labelledby="Authority_control_frameless_&amp;#124;text-top_&amp;#124;10px_&amp;#124;alt=Edit_this_at_Wikidata_&amp;#124;link=https&amp;#58;//www.wikidata.org/wiki/Q36#identifiers&amp;#124;Edit_this_at_Wikidata" style="padding:3px"><table class="nowraplinks hlist mw-collapsible autocollapse navbox-inner mw-made-collapsible mw-collapsed" style="border-spacing:0;background:transparent;color:inherit"><tbody><tr><th scope="col" class="navbox-title" colspan="2"><span class="mw-collapsible-toggle mw-collapsible-toggle-default mw-collapsible-toggle-collapsed" role="button" tabindex="0" aria-expanded="false"><a class="mw-collapsible-text">Expand</a></span><div id="Authority_control_frameless_&amp;#124;text-top_&amp;#124;10px_&amp;#124;alt=Edit_this_at_Wikidata_&amp;#124;link=https&amp;#58;//www.wikidata.org/wiki/Q36#identifiers&amp;#124;Edit_this_at_Wikidata" style="font-size:114%;margin:0 4em"><a href="/wiki/Help:Authority_control" title="Help:Authority control">Authority control</a> <a href="https://www.wikidata.org/wiki/Q36#identifiers" title="Edit this at Wikidata"><img alt="Edit this at Wikidata" src="//upload.wikimedia.org/wikipedia/commons/thumb/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg/10px-OOjs_UI_icon_edit-ltr-progressive.svg.png" decoding="async" width="10" height="10" style="vertical-align: text-top" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg/15px-OOjs_UI_icon_edit-ltr-progressive.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg/20px-OOjs_UI_icon_edit-ltr-progressive.svg.png 2x" data-file-width="20" data-file-height="20"></a></div></th></tr><tr style="display: none;"><th scope="row" class="navbox-group" style="width:1%">General</th><td class="navbox-list-with-group navbox-list navbox-odd" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a href="/wiki/ISNI_(identifier)" class="mw-redirect" title="ISNI (identifier)">ISNI</a>
<ul><li><span class="uid"><a rel="nofollow" class="external text" href="https://isni.org/isni/0000000404710018">1</a></span></li>
<li><span class="uid"><a rel="nofollow" class="external text" href="https://isni.org/isni/000000012293278X">2</a></span></li></ul></li>
<li><a href="/wiki/VIAF_(identifier)" class="mw-redirect" title="VIAF (identifier)">VIAF</a>
<ul><li><span class="uid"><a rel="nofollow" class="external text" href="https://viaf.org/viaf/141810140">1</a></span></li></ul></li>
<li><span class="uid"><a rel="nofollow" class="external text" href="https://www.worldcat.org/identities/viaf-141810140/">WorldCat</a></span></li></ul>
</div></td></tr><tr style="display: none;"><th scope="row" class="navbox-group" style="width:1%">National libraries</th><td class="navbox-list-with-group navbox-list navbox-even" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><span class="uid"><a rel="nofollow" class="external text" href="https://catalogue.bnf.fr/ark:/12148/cb11880842g">France</a> <a rel="nofollow" class="external text" href="https://data.bnf.fr/ark:/12148/cb11880842g">(data)</a></span></li>
<li><span class="uid"><a rel="nofollow" class="external text" href="https://d-nb.info/gnd/4046496-9">Germany</a></span></li>
<li><span class="uid"><a rel="nofollow" class="external text" href="https://id.loc.gov/authorities/names/n79131071">United States</a></span></li>
<li><span class="uid"><a rel="nofollow" class="external text" href="https://id.ndl.go.jp/auth/ndlna/00569130">Japan</a></span></li>
<li><span class="uid"><a rel="nofollow" class="external text" href="https://aleph.nkp.cz/F/?func=find-c&amp;local_base=aut&amp;ccl_term=ica=ge130478&amp;CON_LNG=ENG">Czech Republic</a></span></li>
<li><span class="uid"><a rel="nofollow" class="external text" href="http://mak.bn.org.pl/cgi-bin/KHW/makwww.exe?BM=1&amp;NU=1&amp;IM=4&amp;WI=9810547738505606">Poland</a></span></li></ul>
</div></td></tr><tr style="display: none;"><th scope="row" class="navbox-group" style="width:1%">Other</th><td class="navbox-list-with-group navbox-list navbox-odd" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><span class="uid"><a rel="nofollow" class="external text" href="http://id.worldcat.org/fast/1206891/">Faceted Application of Subject Terminology</a></span></li>
<li><span class="uid"><a rel="nofollow" class="external text" href="https://hls-dhs-dss.ch/fr/articles/003367">Historical Dictionary of Switzerland</a></span></li>
<li><span class="uid"><a href="/wiki/MBAREA_(identifier)" class="mw-redirect" title="MBAREA (identifier)">MusicBrainz</a> <a rel="nofollow" class="external text" href="https://musicbrainz.org/area/dd7f80c8-f017-3d01-8608-2a8c9c32b954">area</a></span></li>
<li><span class="uid"><a rel="nofollow" class="external text" href="https://catalog.archives.gov/id/10045341">National Archives (US)</a></span></li>
<li><a href="/w/index.php?title=RISM_(identifier)&amp;action=edit&amp;redlink=1" class="new" title="RISM (identifier) (not yet started)">RISM (France)</a>
<ul><li><span class="uid"><a rel="nofollow" class="external text" href="https://opac.rism.info/search?id=ks31674">1</a></span></li></ul></li>
<li><a href="/wiki/RERO_(identifier)" title="RERO (identifier)">RERO (Switzerland)</a>
<ul><li><span class="uid"><a rel="nofollow" class="external text" href="http://data.rero.ch/02-A000131730">1</a></span></li></ul></li>
<li><a href="/wiki/SUDOC_(identifier)" class="mw-redirect" title="SUDOC (identifier)">SUDOC (France)</a>
<ul><li><span class="uid"><a rel="nofollow" class="external text" href="https://www.idref.fr/02658994X">1</a></span></li></ul></li>
<li><span class="uid"><a rel="nofollow" class="external text" href="https://islamansiklopedisi.org.tr/polonya">İslâm Ansiklopedisi</a></span></li></ul>
</div></td></tr></tbody></table></div>
<!-- 
NewPP limit report
Parsed by mw1365
Cached time: 20220429200744
Cache expiry: 1814400
Reduced expiry: false
Complications: [vary‐revision‐sha1]
CPU time usage: 1.667 seconds
Real time usage: 1.925 seconds
Preprocessor visited node count: 5409/1000000
Post‐expand include size: 151310/2097152 bytes
Template argument size: 14513/2097152 bytes
Highest expansion depth: 18/100
Expensive parser function count: 26/500
Unstrip recursion depth: 1/20
Unstrip post‐expand size: 49826/5000000 bytes
Lua time usage: 1.015/10.000 seconds
Lua memory usage: 17862378/52428800 bytes
Lua Profile:
    ?                                                                220 ms       19.0%
    Scribunto_LuaSandboxCallback::callParserFunction                 200 ms       17.2%
    Scribunto_LuaSandboxCallback::gsub                               160 ms       13.8%
    Scribunto_LuaSandboxCallback::getEntityStatements                120 ms       10.3%
    Scribunto_LuaSandboxCallback::getEntity                          120 ms       10.3%
    Scribunto_LuaSandboxCallback::getExpandedArgument                100 ms        8.6%
    recursiveClone <mwInit.lua:41>                                    40 ms        3.4%
    Scribunto_LuaSandboxCallback::loadPHPLibrary                      40 ms        3.4%
    Scribunto_LuaSandboxCallback::getEntityId                         40 ms        3.4%
    <mw.lua:690>                                                      20 ms        1.7%
    [others]                                                         100 ms        8.6%
Number of Wikibase entities loaded: 0/400
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00% 1569.807      1 -total
 47.44%  744.774      3 Template:Infobox
 47.23%  741.374      1 Template:Infobox_country
 20.90%  328.097      1 Template:Authority_control
 17.95%  281.852      1 Template:Reflist
 13.36%  209.733      7 Template:Cite_web
 11.38%  178.575      1 Template:Native_name
 10.82%  169.847      1 Template:Lang
  9.55%  149.871      3 Template:ISO_3166_code
  7.20%  113.026      3 Template:Navbox
-->

<!-- Saved in parser cache with key simplewiki:pcache:idhash:3045-0!canonical and timestamp 20220429200742 and revision id 8063612. Serialized with JSON.
 -->
</div>''')
print(output.text)
print(output.data)