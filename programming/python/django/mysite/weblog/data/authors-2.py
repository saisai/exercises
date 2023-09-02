from bs4 import BeautifulSoup

authors = """
<div class="mw-parser-output"><p>This page provides a list of <a href="/wiki/Novelist" title="Novelist">novelists</a> who have written <a href="/wiki/Historical_novel" class="mw-redirect" title="Historical novel">historical novels</a>. Countries named are where they <i>worked</i> for longer periods. Alternative names appear before the dates.
</p>
<div role="note" class="hatnote navigation-not-searchable plainlinks">This list is <a href="/wiki/Wikipedia:WikiProject_Lists#Incomplete_lists" title="Wikipedia:WikiProject Lists">incomplete</a>; you can help by <a class="external text" href="https://en.wikipedia.org/w/index.php?title=List_of_historical_novelists&amp;action=edit">adding missing items</a> with <a href="/wiki/Wikipedia:Reliable_sources" title="Wikipedia:Reliable sources">reliable sources</a>.</div>
<style data-mw-deduplicate="TemplateStyles:r1018014301">@media all and (max-width:719px){body.skin-minerva .mw-parser-output .tocright{display:none}}.mw-parser-output .tocright{float:right;clear:right;width:auto;background:none;padding:.5em 0 .8em 1.4em;margin-bottom:.5em}.mw-parser-output .tocright-clear-left{clear:left}.mw-parser-output .tocright-clear-both{clear:both}.mw-parser-output .tocright-clear-none{clear:none}</style><div class="tocright" style=""><div id="toc" class="toc" role="navigation" aria-labelledby="mw-toc-heading"><input type="checkbox" role="button" id="toctogglecheckbox" class="toctogglecheckbox" style="display:none"><div class="toctitle" lang="en" dir="ltr"><h2 id="mw-toc-heading">Contents</h2><span class="toctogglespan"><label class="toctogglelabel" for="toctogglecheckbox"></label></span></div>
<ul>
<li class="toclevel-1 tocsection-1"><a href="#A"><span class="tocnumber">1</span> <span class="toctext">A</span></a></li>
<li class="toclevel-1 tocsection-2"><a href="#B"><span class="tocnumber">2</span> <span class="toctext">B</span></a></li>
<li class="toclevel-1 tocsection-3"><a href="#C"><span class="tocnumber">3</span> <span class="toctext">C</span></a></li>
<li class="toclevel-1 tocsection-4"><a href="#D"><span class="tocnumber">4</span> <span class="toctext">D</span></a></li>
<li class="toclevel-1 tocsection-5"><a href="#E"><span class="tocnumber">5</span> <span class="toctext">E</span></a></li>
<li class="toclevel-1 tocsection-6"><a href="#F"><span class="tocnumber">6</span> <span class="toctext">F</span></a></li>
<li class="toclevel-1 tocsection-7"><a href="#G"><span class="tocnumber">7</span> <span class="toctext">G</span></a></li>
<li class="toclevel-1 tocsection-8"><a href="#H"><span class="tocnumber">8</span> <span class="toctext">H</span></a></li>
<li class="toclevel-1 tocsection-9"><a href="#I"><span class="tocnumber">9</span> <span class="toctext">I</span></a></li>
<li class="toclevel-1 tocsection-10"><a href="#J"><span class="tocnumber">10</span> <span class="toctext">J</span></a></li>
<li class="toclevel-1 tocsection-11"><a href="#K"><span class="tocnumber">11</span> <span class="toctext">K</span></a></li>
<li class="toclevel-1 tocsection-12"><a href="#L"><span class="tocnumber">12</span> <span class="toctext">L</span></a></li>
<li class="toclevel-1 tocsection-13"><a href="#M"><span class="tocnumber">13</span> <span class="toctext">M</span></a></li>
<li class="toclevel-1 tocsection-14"><a href="#N"><span class="tocnumber">14</span> <span class="toctext">N</span></a></li>
<li class="toclevel-1 tocsection-15"><a href="#O"><span class="tocnumber">15</span> <span class="toctext">O</span></a></li>
<li class="toclevel-1 tocsection-16"><a href="#P"><span class="tocnumber">16</span> <span class="toctext">P</span></a></li>
<li class="toclevel-1 tocsection-17"><a href="#Q"><span class="tocnumber">17</span> <span class="toctext">Q</span></a></li>
<li class="toclevel-1 tocsection-18"><a href="#R"><span class="tocnumber">18</span> <span class="toctext">R</span></a></li>
<li class="toclevel-1 tocsection-19"><a href="#S"><span class="tocnumber">19</span> <span class="toctext">S</span></a></li>
<li class="toclevel-1 tocsection-20"><a href="#T"><span class="tocnumber">20</span> <span class="toctext">T</span></a></li>
<li class="toclevel-1 tocsection-21"><a href="#U"><span class="tocnumber">21</span> <span class="toctext">U</span></a></li>
<li class="toclevel-1 tocsection-22"><a href="#V"><span class="tocnumber">22</span> <span class="toctext">V</span></a></li>
<li class="toclevel-1 tocsection-23"><a href="#W"><span class="tocnumber">23</span> <span class="toctext">W</span></a></li>
<li class="toclevel-1 tocsection-24"><a href="#Y"><span class="tocnumber">24</span> <span class="toctext">Y</span></a></li>
<li class="toclevel-1 tocsection-25"><a href="#Z"><span class="tocnumber">25</span> <span class="toctext">Z</span></a></li>
<li class="toclevel-1 tocsection-26"><a href="#See_also"><span class="tocnumber">26</span> <span class="toctext">See also</span></a></li>
</ul>
</div>
</div>
<h2><span class="mw-headline" id="A">A</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=List_of_historical_novelists&amp;action=edit&amp;section=1" title="Edit section: A">edit</a><span class="mw-editsection-bracket">]</span></span></h2>
<style data-mw-deduplicate="TemplateStyles:r998391716">.mw-parser-output .div-col{margin-top:0.3em;column-width:30em}.mw-parser-output .div-col-small{font-size:90%}.mw-parser-output .div-col-rules{column-rule:1px solid #aaa}.mw-parser-output .div-col dl,.mw-parser-output .div-col ol,.mw-parser-output .div-col ul{margin-top:0}.mw-parser-output .div-col li,.mw-parser-output .div-col dd{page-break-inside:avoid;break-inside:avoid-column}</style><div class="div-col" style="column-width: 20em;">
<ul><li><a href="/wiki/Leopoldo_Alas" title="Leopoldo Alas">Leopoldo Alas</a> (1852–1901, Spain)</li>
<li><a href="/wiki/Edwin_Abbott_Abbott" title="Edwin Abbott Abbott">Edwin Abbott</a> (1838–1926, England)</li>
<li><a href="/wiki/Peter_Ackroyd" title="Peter Ackroyd">Peter Ackroyd</a> (born 1949, England)</li>
<li><a href="/wiki/Gil_Adamson" title="Gil Adamson">Gil Adamson</a> (born 1961, Canada)</li>
<li><a href="/wiki/Emma_Adler" title="Emma Adler">Emma Adler</a> (1858–1935, Austria)</li>
<li><a href="/wiki/Lucy_Aikin" title="Lucy Aikin">Lucy Aikin</a> (1781–1864, England)</li>
<li><a href="/wiki/William_Harrison_Ainsworth" title="William Harrison Ainsworth">William Harrison Ainsworth</a> (1805–1882, England)</li>
<li><a href="/wiki/Jan_van_Aken_(writer)" title="Jan van Aken (writer)">Jan van Aken</a> (born 1961, Netherlands)</li>
<li><a href="/wiki/Bruce_Alexander_Cook" title="Bruce Alexander Cook">Bruce Alexander</a> (1932–2003, US)</li>
<li><a href="/wiki/Joseph_Alexander_Altsheler" title="Joseph Alexander Altsheler">Joseph Alexander Altsheler</a> (1862–1919, US)</li>
<li><a href="/wiki/Miriam_Alexander" title="Miriam Alexander">Miriam Alexander</a> (born 1879, England)</li>
<li><a href="/wiki/Willibald_Alexis" title="Willibald Alexis">Willibald Alexis</a> (1798–1871, Germany)</li>
<li><a href="/wiki/Alexander_Allardyce_(author)" title="Alexander Allardyce (author)">Alexander Allardyce</a> (1846–1896, Scotland)</li>
<li><a href="/wiki/Barbara_Allen_(writer)" class="mw-redirect" title="Barbara Allen (writer)">Barbara Allen</a> (1914–1986, England)</li>
<li><a href="/wiki/Isabel_Allende" title="Isabel Allende">Isabel Allende</a> (born 1942, Chile)</li>
<li><a href="/wiki/Joseph_Alexander_Altsheler" title="Joseph Alexander Altsheler">Joseph Alexander Altsheler</a> (1862–1919, US)</li>
<li><a href="/wiki/Anurag_Anand" title="Anurag Anand">Anurag Anand</a> (born 1978, India)</li>
<li><a href="/wiki/Valerie_Anand" title="Valerie Anand">Valerie Anand</a> (born 1937, England)</li>
<li><a href="/wiki/Catherine_Anderson" title="Catherine Anderson">Catherine Anderson</a> (born 1948, US)</li>
<li><a href="/wiki/Poul_Anderson" title="Poul Anderson">Poul Anderson</a> (1926–2001, US)</li>
<li><a href="/wiki/Sam_Angus_(writer)" title="Sam Angus (writer)">Sam Angus</a> (born 1967, England)</li>
<li><a href="/wiki/Evelyn_Anthony" title="Evelyn Anthony">Evelyn Anthony</a> (1926–2018, England)</li>
<li><a href="/wiki/P._C._Doherty" class="mw-redirect" title="P. C. Doherty">Anna Apostolou</a> (born 1946, England)</li>
<li><a href="/wiki/Sawako_Ariyoshi" title="Sawako Ariyoshi">Sawako Ariyoshi</a> (有吉佐和子, 1931–1984, Japan)</li>
<li><a href="/wiki/Rebecca_Agatha_Armour" title="Rebecca Agatha Armour">Rebecca Agatha Armour</a> (1845–1891, Canada)</li>
<li><a href="/wiki/Jir%C5%8D_Asada" title="Jirō Asada">Jirō Asada</a> (born 1951, Japan)</li>
<li><a href="/wiki/Makate_Asai" title="Makate Asai">Makate Asai</a> (朝井まかて, born 1959, Japan)</li>
<li><a href="/wiki/Matilde_Asensi" title="Matilde Asensi">Matilde Asensi</a> (born 1962, Spain)</li>
<li><a href="/wiki/Margaret_Atwood" title="Margaret Atwood">Margaret Atwood</a> (born 1939, Canada)</li>
<li><a href="/wiki/Jean_M._Auel" title="Jean M. Auel">Jean M. Auel</a> (born 1936, US)</li>
<li><a href="/wiki/Lynn_Austin" title="Lynn Austin">Lynn Austin</a> (born 1949, US)</li></ul></div>
<h2><span class="mw-headline" id="B">B</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=List_of_historical_novelists&amp;action=edit&amp;section=2" title="Edit section: B">edit</a><span class="mw-editsection-bracket">]</span></span></h2>
<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r998391716"><div class="div-col" style="column-width: 20em;">
<ul><li><a href="/wiki/Balakumaran" title="Balakumaran">Balakumaran</a> (1946–2018, India)</li>
<li><a href="/wiki/Mary_Balogh" title="Mary Balogh">Mary Balogh</a> (born 1944, Wales/Canada)</li>
<li><a href="/wiki/Kathleen_Baldwin" title="Kathleen Baldwin">Kathleen Baldwin</a> (living, US)</li>
<li><a href="/wiki/Andrew_Balfour" title="Andrew Balfour">Andrew Balfour</a> (1873–1931, Scotland)</li>
<li><a href="/wiki/Robert_Michael_Ballantyne" class="mw-redirect" title="Robert Michael Ballantyne">Robert Michael Ballantyne</a> (1825–1894, Scotland)</li>
<li><a href="/wiki/Sharadindu_Bandyopadhyay" title="Sharadindu Bandyopadhyay">Sharadindu Bandyopadhyay</a> (1899–1970, India)</li>
<li><a href="/wiki/Mikl%C3%B3s_B%C3%A1nffy" title="Miklós Bánffy">Miklós Bánffy</a> (1873–1950, Hungary)</li>
<li><a href="/wiki/John_Banim" title="John Banim">John Banim</a> (1798–1842, Ireland)</li>
<li><a href="/wiki/Isabella_Banks" title="Isabella Banks">Isabella Banks</a> (1821–1897, England)</li>
<li><a href="/wiki/Sabine_Baring-Gould" title="Sabine Baring-Gould">Sabine Baring-Gould</a> (1834–1924, England)</li>
<li><a href="/wiki/Pat_Barker" title="Pat Barker">Pat Barker</a> (born 1943, England)</li>
<li><a href="/wiki/Vasil_Barnovi" title="Vasil Barnovi">Vasil Barnovi</a> (1856–1934, Georgia/Soviet Union)</li>
<li><a href="/wiki/Sam_Barone" title="Sam Barone">Sam Barone</a> (living, US)</li>
<li><a href="/wiki/T._A._Barron" title="T. A. Barron">T. A. Barron</a> (born 1952, US)</li>
<li><a href="/wiki/Adolf_Bartels" title="Adolf Bartels">Adolf Bartels</a> (1862–1945, Germany)</li>
<li><a href="/wiki/Hans_Baumann_(writer)" title="Hans Baumann (writer)">Hans Baumann</a> (1914–1988, Germany)</li>
<li><a href="/wiki/Nina_Bawden" title="Nina Bawden">Nina Bawden</a> (1925–2012, England)</li>
<li><a href="/wiki/Ada_Ellen_Bayly" title="Ada Ellen Bayly">Ada Ellen Bayly</a> (1857–1903, England), pseudonym of Edna Lyall</li>
<li><a href="/wiki/Thea_Beckman" title="Thea Beckman">Thea Beckman</a> (1923–2004, Netherlands)</li>
<li><a href="/wiki/Frank_Beddor" title="Frank Beddor">Frank Beddor</a> (born 1958, US)</li>
<li><a href="/wiki/Frans_G._Bengtsson" title="Frans G. Bengtsson">Frans G. Bengtsson</a> (1894–1954, Sweden)</li>
<li><a href="/wiki/Robert_Hugh_Benson" title="Robert Hugh Benson">Robert Hugh Benson</a> (1871–1914, England/Italy)</li>
<li><a href="/wiki/Phyllis_Bentley" title="Phyllis Bentley">Phyllis Bentley</a> (1894–1977, England)</li>
<li><a href="/wiki/Sir_Walter_Besant" class="mw-redirect" title="Sir Walter Besant">Sir Walter Besant</a> (1836–1901, England)</li>
<li><a href="/wiki/Tom_Bevan" title="Tom Bevan">Tom Bevan</a> (1868–1938, England)</li>
<li><a href="/wiki/Paul_Biegel" title="Paul Biegel">Paul Biegel</a> (1925–2006, Netherlands)</li>
<li><a href="/wiki/Charlotte_Bingham" title="Charlotte Bingham">Charlotte Bingham</a> (born 1942, England)</li>
<li><a href="/wiki/L%C3%A1szl%C3%B3_Z._Bit%C3%B3" title="László Z. Bitó">László Z. Bitó</a> (born 1934, Hungary)</li>
<li><a href="/wiki/R._D._Blackmore" title="R. D. Blackmore">R. D. Blackmore</a> (1825–1900, England)</li>
<li><a href="/wiki/Dennis_Bock" title="Dennis Bock">Dennis Bock</a> (born 1964, Canada)</li>
<li><a href="/wiki/Emily_Bold" title="Emily Bold">Emily Bold</a> (born 1980, Germany)</li>
<li><a href="/wiki/Elizabeth_Bonh%C3%B4te" title="Elizabeth Bonhôte">Elizabeth Bonhôte</a> (1744–1818, England)</li>
<li><a href="/wiki/Alice_Borchardt" title="Alice Borchardt">Alice Borchardt</a> (1939–2007, US)</li>
<li><a href="/wiki/John_Boyne" title="John Boyne">John Boyne</a> (born 1971, Ireland)</li>
<li><a href="/wiki/Paula_Brackston" title="Paula Brackston">Paula Brackston</a> (living, England)</li>
<li><a href="/wiki/Alan_Bradley_(writer)" title="Alan Bradley (writer)">Alan Bradley</a> (born 1938, Canada)</li>
<li><a href="/wiki/Gillian_Bradshaw" title="Gillian Bradshaw">Gillian Bradshaw</a> (born 1956, US)</li>
<li><a href="/wiki/Anna_Eliza_Bray" title="Anna Eliza Bray">Anna Eliza Bray</a> (1790–1883, England)</li>
<li><a href="/wiki/Wallace_Breem" title="Wallace Breem">Wallace Breem</a> (1926–1990, England)</li>
<li><a href="/wiki/Frederick_Sadleir_Brereton" title="Frederick Sadleir Brereton">Frederick Sadleir Brereton</a> (1852–1957, England)</li>
<li><a href="/wiki/Emily_Brightwell" class="mw-redirect" title="Emily Brightwell">Emily Brightwell</a> (Cheryl Lanham, born 1948, US)</li>
<li><a href="/wiki/Connie_Brockway" title="Connie Brockway">Connie Brockway</a> (born 1954, US)</li>
<li><a href="/wiki/Geraldine_Brooks_(writer)" title="Geraldine Brooks (writer)">Geraldine Brooks</a> (born 1955, Australia/US)</li>
<li><a href="/wiki/D._K._Broster" title="D. K. Broster">D. K. Broster</a> (1877–1950, England)</li>
<li><a href="/wiki/Valery_Bryusov" title="Valery Bryusov">Valery Bryusov</a> (1873–1924, Russia/Soviet Union)</li>
<li><a href="/wiki/John_Buchan" title="John Buchan">John Buchan</a> (1875–1940, Scotland)</li>
<li><a href="/wiki/Valerie_Anand" title="Valerie Anand">Fiona Buckley</a> (born 1937, England)</li>
<li><a href="/wiki/Frederick_Buechner" title="Frederick Buechner">Frederick Buechner</a> (born 1926, US)</li>
<li><a href="/wiki/Emma_Bull" title="Emma Bull">Emma Bull</a> (born 1954, US)</li>
<li><a href="/wiki/Edward_Bulwer-Lytton,_1st_Baron_Lytton" class="mw-redirect" title="Edward Bulwer-Lytton, 1st Baron Lytton">Edward Bulwer-Lytton</a> (1803–1873, England)</li>
<li><a href="/wiki/Eleanor_Hibbert" title="Eleanor Hibbert">Eleanor Burford</a> (1906–1993, England)</li>
<li><a href="/wiki/Anthony_Burgess" title="Anthony Burgess">Anthony Burgess</a> (1917–1993, England)</li>
<li><a href="/wiki/James_Lee_Burke" title="James Lee Burke">James Lee Burke</a> (born 1936, US)</li>
<li><a href="/wiki/Edgar_Rice_Burroughs" title="Edgar Rice Burroughs">Edgar Rice Burroughs</a> (1875–1950, US)</li>
<li><a href="/wiki/Hester_Burton" title="Hester Burton">Hester Burton</a> (1913–2000, England)</li>
<li><a href="/wiki/Jessie_Burton" title="Jessie Burton">Jessie Burton</a> (born 1982, England)</li>
<li><a href="/wiki/Frederick_Busch" title="Frederick Busch">Frederick Busch</a> (1941–2006, US)</li>
<li><a href="/wiki/A._S._Byatt" title="A. S. Byatt">A. S. Byatt</a> (born 1936, England)</li>
<li><a href="/wiki/Elizabeth_Byrd" title="Elizabeth Byrd">Elizabeth Byrd</a> (1912–1989, US)</li></ul></div>
<h2><span class="mw-headline" id="C">C</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=List_of_historical_novelists&amp;action=edit&amp;section=3" title="Edit section: C">edit</a><span class="mw-editsection-bracket">]</span></span></h2>
<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r998391716"><div class="div-col" style="column-width: 20em;">
<ul><li><a href="/wiki/Hall_Caine" title="Hall Caine">Hall Caine</a> (1853–1931, England/Isle of Man)</li>
<li><a href="/wiki/Italo_Calvino" title="Italo Calvino">Italo Calvino</a> (1923–1985, Italy)</li>
<li><a href="/wiki/Peter_Carey_(novelist)" title="Peter Carey (novelist)">Peter Carey</a> (born 1943, Australia)</li>
<li><a href="/wiki/William_Carleton" title="William Carleton">William Carleton</a> (1794–1869, Ireland)</li>
<li><a href="/wiki/Liz_Carlyle" title="Liz Carlyle">Liz Carlyle</a> (born 1958, US)</li>
<li><a href="/wiki/Caleb_Carr" title="Caleb Carr">Caleb Carr</a> (born 1955, US)</li>
<li><a href="/wiki/John_Dickson_Carr" title="John Dickson Carr">John Dickson Carr</a> (1906–1977, US)</li>
<li><a href="/wiki/Eleanor_Hibbert" title="Eleanor Hibbert">Philippa Carr</a> (1906–1993, England)</li>
<li><a href="/wiki/Catherine_Carswell" title="Catherine Carswell">Catherine Carswell</a> (1879–1946, Scotland)</li>
<li><a href="/wiki/Willa_Cather" title="Willa Cather">Willa Cather</a> (1873–1947, US)</li>
<li><a href="/wiki/Nancy_Cato" title="Nancy Cato">Nancy Cato</a> (1917–2000, Australia)</li>
<li><a href="/wiki/Juraj_%C4%8Cerven%C3%A1k" title="Juraj Červenák">Juraj Červenák</a> (born 1974, Czechoslovakia/Slovakia)</li>
<li><a href="/wiki/Elizabeth_Chadwick" title="Elizabeth Chadwick">Elizabeth Chadwick</a> (born 1957, England)</li>
<li><a href="/wiki/Somerset_de_Chair" title="Somerset de Chair">Somerset de Chair</a> (1911–1995, England)</li>
<li><a href="/wiki/Aleksey_Chapygin" title="Aleksey Chapygin">Aleksey Chapygin</a> (1870–1937, Russia/Soviet Union)</li>
<li><a href="/wiki/Isabel_Cheix" title="Isabel Cheix">Isabel Cheix</a> (1839–1899, Spain)</li>
<li><a href="/wiki/Tracy_Chevalier" title="Tracy Chevalier">Tracy Chevalier</a> (born 1962, US)</li>
<li><a href="/wiki/Alfred_John_Church" title="Alfred John Church">Alfred John Church</a> (1829–1912, England)</li>
<li><a href="/wiki/Winston_Churchill_(novelist)" title="Winston Churchill (novelist)">Winston Churchill</a> (1871–1947, US)</li>
<li><a href="/wiki/Alys_Clare" title="Alys Clare">Alys Clare</a> (Elizabeth Harris, born 1944, England)</li>
<li><a href="/wiki/Mrs._Henry_Clarke" title="Mrs. Henry Clarke">Mrs. Henry Clarke</a> (1853–1908, England)</li>
<li><a href="/wiki/Marcus_Clarke" title="Marcus Clarke">Marcus Clarke</a> (1846–1881, Australia)</li>
<li><a href="/wiki/Susanna_Clarke" title="Susanna Clarke">Susanna Clarke</a> (born 1959, England)</li>
<li><a href="/wiki/James_Clavell" title="James Clavell">James Clavell</a> (1924–1994, England/US)</li>
<li><a href="/wiki/Brian_Cleeve" title="Brian Cleeve">Brian Cleeve</a> (1921–2003, England)</li>
<li><a href="/wiki/Paul_C._Doherty" title="Paul C. Doherty">Michael Clynes</a> (born 1946, England)</li>
<li><a href="/wiki/Ioan_Mihai_Cochinescu" title="Ioan Mihai Cochinescu">Ioan Mihai Cochinescu</a> (born 1951, Romania)</li>
<li><a href="/wiki/Jonathan_Coe" title="Jonathan Coe">Jonathan Coe</a> (born 1961, England)</li>
<li><a href="/wiki/Jan_Coffey" title="Jan Coffey">Jan Coffey</a> (living, US, f), pseudonym of married couple</li>
<li><a href="/wiki/Christabel_Rose_Coleridge" title="Christabel Rose Coleridge">Christabel Rose Coleridge</a> (1843–1921, England)</li>
<li><a href="/wiki/Wilkie_Collins" title="Wilkie Collins">Wilkie Collins</a> (1824–1889, England)</li>
<li><a href="/wiki/Padraic_Colum" title="Padraic Colum">Padraic Colum</a> (1881–1972, Ireland/US)</li>
<li><a href="/wiki/Maryse_Cond%C3%A9" title="Maryse Condé">Maryse Condé</a> (born 1937, Guadeloupe)</li>
<li><a href="/wiki/Marita_Conlon-McKenna" title="Marita Conlon-McKenna">Marita Conlon-McKenna</a> (born 1956, Ireland)</li>
<li><a href="/wiki/Joseph_Conrad" title="Joseph Conrad">Joseph Conrad</a> (1857–1924, England)</li>
<li><a href="/wiki/Judith_Cook" title="Judith Cook">Judith Cook</a> (1933–2004, England)</li>
<li><a href="/wiki/Barbara_Cooney" title="Barbara Cooney">Barbara Cooney</a> (1917–2000, US)</li>
<li><a href="/wiki/James_Fenimore_Cooper" title="James Fenimore Cooper">James Fenimore Cooper</a> (1789–1851, US)</li>
<li><a href="/wiki/Bernard_Cornwell" title="Bernard Cornwell">Bernard Cornwell</a> (born 1944, England)</li>
<li><a href="/wiki/Thomas_B._Costain" title="Thomas B. Costain">Thomas B. Costain</a> (1885–1965, Canada/US)</li>
<li><a href="/wiki/Catherine_Coulter" title="Catherine Coulter">Catherine Coulter</a> (born 1942, US)</li>
<li><a href="/wiki/Jim_Crace" title="Jim Crace">Jim Crace</a> (born 1946, England)</li>
<li><a href="/wiki/Helen_Craik" title="Helen Craik">Helen Craik</a> (c. 1751–1825, Scotland/England)</li>
<li><a href="/wiki/Jasmine_Cresswell" title="Jasmine Cresswell">Jasmine Cresswell</a> (born 1941, Wales)</li>
<li><a href="/wiki/Donna_Woolfolk_Cross" title="Donna Woolfolk Cross">Donna Woolfolk Cross</a> (born 1947, US)</li>
<li><a href="/wiki/Andrew_Crumey" title="Andrew Crumey">Andrew Crumey</a> (born 1961, Scotland)</li>
<li><a href="/wiki/Karen_Cushman" title="Karen Cushman">Karen Cushman</a> (born 1941, US)</li>
<li><a href="/wiki/Catherine_Cuthbertson" title="Catherine Cuthbertson">Catherine Cuthbertson</a> (c. 1775–1842, England)</li></ul></div>
<h2><span class="mw-headline" id="D">D</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=List_of_historical_novelists&amp;action=edit&amp;section=4" title="Edit section: D">edit</a><span class="mw-editsection-bracket">]</span></span></h2>
<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r998391716"><div class="div-col" style="column-width: 20em;">
<ul><li><a href="/wiki/Maria_D%C4%85browska" title="Maria Dąbrowska">Maria Dąbrowska</a> (1889–1965, Poland)</li>
<li><a href="/wiki/Felix_Dahn" title="Felix Dahn">Felix Dahn</a> (1834–1912, Germany)</li>
<li><a href="/wiki/Alice_Dalgliesh" title="Alice Dalgliesh">Alice Dalgliesh</a> (1893–1979, US)</li>
<li><a href="/wiki/Grigory_Danilevsky" title="Grigory Danilevsky">Grigory Danilevsky</a> (1829–1890, Ukraine/Russian Empire)</li>
<li><a href="/wiki/Lindsey_Davis" title="Lindsey Davis">Lindsey Davis</a> (born 1949, England)</li>
<li><a href="/wiki/William_Stearns_Davis" title="William Stearns Davis">William Stearns Davis</a> (1877–1930, US)</li>
<li><a href="/wiki/Louis_de_Berni%C3%A8res" title="Louis de Bernières">Louis de Bernières</a> (born 1954, England)</li>
<li><a href="/wiki/Celeste_De_Blasis" title="Celeste De Blasis">Celeste De Blasis</a> (1946–2001, US)</li>
<li><a href="/wiki/L._Sprague_de_Camp" title="L. Sprague de Camp">L. Sprague de Camp</a> (1907–2000, US)</li>
<li><a href="/wiki/Jan_de_Hartog" title="Jan de Hartog">Jan de Hartog</a> (1914–2002, Netherlands)</li>
<li><a href="/wiki/Len_Deighton" title="Len Deighton">Len Deighton</a> (born 1929, England)</li>
<li><a href="/wiki/Miguel_Delibes" title="Miguel Delibes">Miguel Delibes</a> (1920–2010, Spain)</li>
<li><a href="/wiki/Don_DeLillo" title="Don DeLillo">Don DeLillo</a> (born 1936, US)</li>
<li><a href="/wiki/Penelope_Delta" title="Penelope Delta">Penelope Delta</a> (1874–1941, Greece)</li>
<li><a href="/wiki/Zs%C3%B3fia_D%C3%A9nes" title="Zsófia Dénes">Zsófia Dénes</a> (1885–1987, Hungary)</li>
<li><a href="/wiki/August_Derleth" title="August Derleth">August Derleth</a> (1909–1971, US)</li>
<li><a href="/wiki/Jude_Deveraux" title="Jude Deveraux">Jude Deveraux</a> (born 1947, US)</li>
<li><a href="/wiki/Patrick_deWitt" title="Patrick deWitt">Patrick deWitt</a> (born 1975, Canada)</li>
<li><a href="/wiki/Charles_Dezobry" title="Charles Dezobry">Charles Dezobry</a> (1798–1871, France)</li>
<li><a href="/wiki/Anita_Diamant" title="Anita Diamant">Anita Diamant</a> (born 1951, US)</li>
<li><a href="/wiki/Graham_Diamond" title="Graham Diamond">Graham Diamond</a> (born 1945, England)</li>
<li><a href="/wiki/Charles_Dickens" title="Charles Dickens">Charles Dickens</a> (1812–1870, England)</li>
<li><a href="/wiki/Benjamin_Disraeli" title="Benjamin Disraeli">Benjamin Disraeli</a> (1804–1881, England)</li>
<li><a href="/wiki/E._L._Doctorow" title="E. L. Doctorow">E. L. Doctorow</a> (1931–2015, US)</li>
<li><a href="/wiki/Mary_Mapes_Dodge" title="Mary Mapes Dodge">Mary Mapes Dodge</a> (1831–1905, US)</li>
<li><a href="/wiki/Anthony_Doerr" title="Anthony Doerr">Anthony Doerr</a> (born 1973, US)</li>
<li><a href="/wiki/Paul_C._Doherty" title="Paul C. Doherty">Paul C. Doherty</a> (born 1946, England)</li>
<li><a href="/wiki/Sir_Arthur_Conan_Doyle" class="mw-redirect" title="Sir Arthur Conan Doyle">Sir Arthur Conan Doyle</a> (1859–1930, Scotland/England)</li>
<li><a href="/wiki/David_Donachie" title="David Donachie">David Donachie</a> (born 1944, Scotland)</li>
<li><a href="/wiki/Angus_Donald" title="Angus Donald">Angus Donald</a> (born 1965, England)</li>
<li><a href="/wiki/Anton_Donchev" title="Anton Donchev">Anton Donchev</a> (born 1930, Bulgaria)</li>
<li><a href="/wiki/Emma_Donoghue" title="Emma Donoghue">Emma Donoghue</a> (born 1969, England/Canada)</li>
<li><a href="/wiki/Thomas_Doubleday" title="Thomas Doubleday">Thomas Doubleday</a> (1790–1870, England)</li>
<li><a href="/wiki/Tonke_Dragt" title="Tonke Dragt">Tonke Dragt</a> (born 1930, Netherlands)</li>
<li><a href="/wiki/Joan_Druett" title="Joan Druett">Joan Druett</a> (living, New Zealand)</li>
<li><a href="/wiki/Anna_Harriett_Drury" title="Anna Harriett Drury">Anna Harriett Drury</a> (1824–1912, England)</li>
<li><a href="/wiki/John_Langalibalele_Dube" title="John Langalibalele Dube">John Langalibalele Dube</a> (1871–1946, South Africa) in <a href="/wiki/Zulu_language" title="Zulu language">isiZulu</a></li>
<li><a href="/wiki/Mar%C3%ADa_Due%C3%B1as" title="María Dueñas">María Dueñas</a> (b. 1964, Spain)</li>
<li><a href="/wiki/Alfred_Duggan" title="Alfred Duggan">Alfred Duggan</a> (1903–1964, England)</li>
<li><a href="/wiki/Alexandre_Dumas,_p%C3%A8re" class="mw-redirect" title="Alexandre Dumas, père">Alexandre Dumas, père</a> (1802–1870, France)</li>
<li><a href="/wiki/Daphne_du_Maurier" title="Daphne du Maurier">Daphne du Maurier</a> (1907–1989, England)</li>
<li><a href="/wiki/Paul_C._Doherty" title="Paul C. Doherty">Ann Dukthas</a> (born 1946, England)</li>
<li><a href="/wiki/Maurice_Druon" title="Maurice Druon">Maurice Druon</a> (1918–2009, France)</li>
<li><a href="/wiki/Dorothy_Dunnett" title="Dorothy Dunnett">Dorothy Dunnett</a> (1923–2001, Scotland)</li>
<li><a href="/wiki/Mary_Durack" title="Mary Durack">Mary Durack</a> (1913–1994, Australia)</li>
<li><a href="/wiki/David_Anthony_Durham" title="David Anthony Durham">David Anthony Durham</a> (born 1969, US)</li></ul></div>
<h2><span class="mw-headline" id="E">E</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=List_of_historical_novelists&amp;action=edit&amp;section=5" title="Edit section: E">edit</a><span class="mw-editsection-bracket">]</span></span></h2>
<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r998391716"><div class="div-col" style="column-width: 20em;">
<ul><li><a href="/wiki/Marion_Eames" title="Marion Eames">Marion Eames</a> (1921–2007, Wales)</li>
<li><a href="/wiki/Georg_Ebers" title="Georg Ebers">Georg Ebers</a> (1837–1898, Germany)</li>
<li><a href="/wiki/Allan_W._Eckert" title="Allan W. Eckert">Allan W. Eckert</a> (1931–2011, US</li>
<li><a href="/wiki/Ernst_Eckstein" title="Ernst Eckstein">Ernst Eckstein</a> (1845–1900, Germany)</li>
<li><a href="/wiki/Umberto_Eco" title="Umberto Eco">Umberto Eco</a> (1932–2016, Italy)</li>
<li><a href="/wiki/John_George_Edgar" title="John George Edgar">John George Edgar</a> (1834–1864, England)</li>
<li><a href="/wiki/Arabella_Edge" title="Arabella Edge">Arabella Edge</a> (living, England/Australia)</li>
<li><a href="/wiki/George_Eliot" title="George Eliot">George Eliot</a> (1819–1880, England)</li>
<li><a href="/wiki/James_Ellroy" title="James Ellroy">James Ellroy</a> (born 1948, US)</li>
<li><a href="/wiki/Sh%C5%ABsaku_End%C5%8D" title="Shūsaku Endō">Shūsaku Endō</a> (遠藤周作, 1923–1996, Japan)</li>
<li><a href="/wiki/J%C3%B3zsef_E%C3%B6tv%C3%B6s" title="József Eötvös">József Eötvös</a> (1813–1871, Hungary)</li>
<li><a href="/wiki/Amy_Ephron" title="Amy Ephron">Amy Ephron</a> (born 1952, US)</li>
<li><a href="/wiki/Erckmann-Chatrian" title="Erckmann-Chatrian">Erckmann-Chatrian</a> (France), pseudonym of <a href="/wiki/%C3%89mile_Erckmann" title="Émile Erckmann">Émile Erckmann</a> (1822–1899) and <a href="/wiki/Alexandre_Chatrian" title="Alexandre Chatrian">Alexandre Chatrian</a> (1826–1890)</li>
<li><a href="/wiki/Rica_Erickson" title="Rica Erickson">Rica Erickson</a> (1908–2009, Australia)</li>
<li><a href="/wiki/I._O._Evans" title="I. O. Evans">I. O. Evans</a> (1894–1977, S Africa/England)</li>
<li><a href="/wiki/Evelyn_Everett-Green" title="Evelyn Everett-Green">Evelyn Everett-Green</a> (1856–1932, England)</li>
<li><a href="/wiki/Elizabeth_Eyre" title="Elizabeth Eyre">Elizabeth Eyre</a> (England), pseudonym of Jill Staynes and <a href="/wiki/Margaret_Storey_(mystery_writer)" class="mw-redirect" title="Margaret Storey (mystery writer)">Margaret Storey</a></li></ul></div>
<h2><span class="mw-headline" id="F">F</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=List_of_historical_novelists&amp;action=edit&amp;section=6" title="Edit section: F">edit</a><span class="mw-editsection-bracket">]</span></span></h2>
<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r998391716"><div class="div-col" style="column-width: 20em;">
<ul><li><a href="/wiki/Michel_Faber" title="Michel Faber">Michel Faber</a> (born 1960, England)</li>
<li><a href="/wiki/Cerridwen_Fallingstar" title="Cerridwen Fallingstar">Cerridwen Fallingstar</a> (born 1952, US)</li>
<li><a href="/wiki/Frederic_William_Farrar" class="mw-redirect" title="Frederic William Farrar">Frederic William Farrar</a> (1831–1903, England)</li>
<li><a href="/wiki/J._G._Farrell" title="J. G. Farrell">J. G. Farrell</a> (1935–1979, England)</li>
<li><a href="/wiki/Penelope_Farmer" title="Penelope Farmer">Penelope Farmer</a> (born 1939, England)</li>
<li><a href="/wiki/Howard_Fast" title="Howard Fast">Howard Fast</a> (1914–2003, US)</li>
<li><a href="/wiki/Sebastian_Faulks" title="Sebastian Faulks">Sebastian Faulks</a> (born 1953, England)</li>
<li><a href="/wiki/Madame_de_la_Fayette" class="mw-redirect" title="Madame de la Fayette">Madame de la Fayette</a> (1634–1693, France)</li>
<li><a href="/wiki/Jane_Feather" title="Jane Feather">Jane Feather</a> (born 1945, England/US)</li>
<li><a href="/wiki/George_Manville_Fenn" title="George Manville Fenn">George Manville Fenn</a> (1831–1909, England)</li>
<li><a href="/wiki/Leon_Feuchtwanger" class="mw-redirect" title="Leon Feuchtwanger">Leon Feuchtwanger</a> (1884–1958, Germany/US)</li>
<li><a href="/wiki/Mrs._E._M._Field" title="Mrs. E. M. Field">Mrs. E. M. Field</a> (1856–1940, Ireland)</li>
<li><a href="/wiki/Charles_Finch" title="Charles Finch">Charles Finch</a> (born 1980, US)</li>
<li><a href="/wiki/Penelope_Fitzgerald" title="Penelope Fitzgerald">Penelope Fitzgerald</a> (1916–2000, England)</li>
<li><a href="/wiki/John_Flanagan_(author)" title="John Flanagan (author)">John Flanagan</a> (born 1944, Australia)</li>
<li><a href="/wiki/Richard_Flanagan" title="Richard Flanagan">Richard Flanagan</a> (born 1961, Australia)</li>
<li><a href="/wiki/Gustave_Flaubert" title="Gustave Flaubert">Gustave Flaubert</a> (1821–1880, France)</li>
<li><a href="/wiki/Katie_Flynn" title="Katie Flynn">Katie Flynn</a> (1936–2019, England)</li>
<li><a href="/wiki/Per_Anders_Fogelstr%C3%B6m" title="Per Anders Fogelström">Per Anders Fogelström</a> (1919–1998, Sweden)</li>
<li><a href="/wiki/Jol%C3%A1n_F%C3%B6ldes" title="Jolán Földes">Jolán Földes</a> (1902–1963, Hungary)</li>
<li><a href="/wiki/Ken_Follett" title="Ken Follett">Ken Follett</a> (born 1949, Wales/England)</li>
<li><a href="/wiki/Theodor_Fontane" title="Theodor Fontane">Theodor Fontane</a> (1819–1898, Germany)</li>
<li><a href="/wiki/Eleanor_Hibbert" title="Eleanor Hibbert">Elburd Ford</a> (1906–1993, England)</li>
<li><a href="/wiki/C._S._Forester" title="C. S. Forester">C. S. Forester</a> (1899–1966, England)</li>
<li><a href="/wiki/William_R._Forstchen" title="William R. Forstchen">William R. Forstchen</a> (born 1950, US,</li>
<li><a href="/wiki/E._M._Foster" title="E. M. Foster">E. M. Foster</a>, Mrs. (fl. late 18th – early 19th cc., England)</li>
<li><a href="/wiki/Karen_Joy_Fowler" title="Karen Joy Fowler">Karen Joy Fowler</a> (born 1950, US)</li>
<li><a href="/wiki/John_Fowles" title="John Fowles">John Fowles</a> (1926–2005, England)</li>
<li><a href="/wiki/Louise_von_Fran%C3%A7ois" title="Louise von François">Louise von François</a> (1817–1893, Germany)</li>
<li><a href="/wiki/Bruno_Frank" title="Bruno Frank">Bruno Frank</a> (1878–1945, Germany/US)</li>
<li><a href="/wiki/George_MacDonald_Fraser" title="George MacDonald Fraser">George MacDonald Fraser</a> (1925–2008, Scotland)</li>
<li><a href="/wiki/Margaret_Frazer" title="Margaret Frazer">Margaret Frazer</a> (1946–2013, US)</li>
<li><a href="/wiki/Gustav_Freytag" title="Gustav Freytag">Gustav Freytag</a> (1816–1895, Germany)</li>
<li><a href="/wiki/Alan_Furst" title="Alan Furst">Alan Furst</a> (born 1941, US)</li>
<li><a href="/wiki/Dale_Furutani" title="Dale Furutani">Dale Furutani</a> (born 1946, US)</li>
<li><a href="/wiki/Sandy_Fussell" title="Sandy Fussell">Sandy Fussell</a> (born 1960, Australia)</li></ul></div>
<h2><span class="mw-headline" id="G">G</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=List_of_historical_novelists&amp;action=edit&amp;section=7" title="Edit section: G">edit</a><span class="mw-editsection-bracket">]</span></span></h2>
<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r998391716"><div class="div-col" style="column-width: 20em;">
<ul><li><a href="/wiki/Benito_P%C3%A9rez_Gald%C3%B3s" title="Benito Pérez Galdós">Benito Pérez Galdós</a> (1843–1920, Spain)</li>
<li><a href="/wiki/Diana_Gabaldon" title="Diana Gabaldon">Diana Gabaldon</a> (born 1952, US)</li>
<li><a href="/wiki/G%C3%A9za_G%C3%A1rdonyi" title="Géza Gárdonyi">Géza Gárdonyi</a> (1863–1922, Hungary)</li>
<li><a href="/wiki/Alan_Garner" title="Alan Garner">Alan Garner</a> (born 1934, England)</li>
<li><a href="/wiki/Elizabeth_Gaskell" title="Elizabeth Gaskell">Elizabeth Gaskell</a> (1810–1865, England)</li>
<li><a href="/wiki/Judith_Gautier" title="Judith Gautier">Judith Gautier</a> (1845–1917, France)</li>
<li><a href="/wiki/Jamila_Gavin" title="Jamila Gavin">Jamila Gavin</a> (born 1941, India/England)</li>
<li><a href="/wiki/Roberta_Gellis" title="Roberta Gellis">Roberta Gellis</a> (1927–2016, US)</li>
<li><a href="/wiki/Margaret_George" title="Margaret George">Margaret George</a> (born 1943, US)</li>
<li><a href="/wiki/Anton_Gill" title="Anton Gill">Anton Gill</a> (living, England)</li>
<li><a href="/wiki/George_Gissing" title="George Gissing">George Gissing</a> (1857–1903, England)</li>
<li><a href="/wiki/Nikolai_Gogol" title="Nikolai Gogol">Nikolai Gogol</a> (1809–1852, Russia)</li>
<li><a href="/wiki/Arthur_Golden" title="Arthur Golden">Arthur Golden</a> (born 1956, US)</li>
<li><a href="/wiki/Julia_Golding" title="Julia Golding">Julia Golding</a> (born 1969, England)</li>
<li><a href="/wiki/William_Golding" title="William Golding">William Golding</a> (1911–1993, England)</li>
<li><a href="/wiki/Jason_Goodwin" title="Jason Goodwin">Jason Goodwin</a> (born 1964, England)</li>
<li><a href="/wiki/Elizabeth_Goudge" title="Elizabeth Goudge">Elizabeth Goudge</a> (1900–1984, England)</li>
<li><a href="/wiki/Iris_Gower" title="Iris Gower">Iris Gower</a> (1935–2010, Wales)</li>
<li><a href="/wiki/Posie_Graeme-Evans" title="Posie Graeme-Evans">Posie Graeme-Evans</a> (born 1952, Australia)</li>
<li><a href="/wiki/Paul_C._Doherty" title="Paul C. Doherty">C. L. Grace</a> (born 1946, England)</li>
<li><a href="/wiki/James_Grant_(1822%E2%80%931887)" title="James Grant (1822–1887)">James Grant</a> (1822–1887, Scotland)</li>
<li><a href="/wiki/Joan_Grant" title="Joan Grant">Joan Grant</a> (1907–1989, England)</li>
<li><a href="/wiki/Ralph_Graves_(writer)" title="Ralph Graves (writer)">Ralph Graves</a> (1924–2013, US)</li>
<li><a href="/wiki/Robert_Graves" title="Robert Graves">Robert Graves</a> (1895–1985, England)</li>
<li><a href="/wiki/Philippa_Gregory" title="Philippa Gregory">Philippa Gregory</a> (born 1954, England)</li>
<li><a href="/wiki/Susanna_Gregory" title="Susanna Gregory">Susanna Gregory</a> (Elizabeth Cruwys, living, England)</li>
<li><a href="/wiki/Gerald_Griffin" title="Gerald Griffin">Gerald Griffin</a> (1803–1840, Ireland)</li>
<li><a href="/wiki/Michael_Cawood_Green" title="Michael Cawood Green">Michael Cawood Green</a> (born 1954, South Africa/England)</li>
<li><a href="/wiki/Sara_Gruen" title="Sara Gruen">Sara Gruen</a> (born 1969, Canada/US)</li>
<li><a href="/wiki/Jan_Guillou" title="Jan Guillou">Jan Guillou</a> (born 1944, France)</li>
<li><a href="/wiki/Yaa_Gyasi" title="Yaa Gyasi">Yaa Gyasi</a> (born 1989, Ghana/US)</li></ul></div>
<h2><span class="mw-headline" id="H">H</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=List_of_historical_novelists&amp;action=edit&amp;section=8" title="Edit section: H">edit</a><span class="mw-editsection-bracket">]</span></span></h2>
<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r998391716"><div class="div-col" style="column-width: 20em;">
<ul><li><a href="/wiki/Hella_Haasse" title="Hella Haasse">Hella Haasse</a> (1918–2011, Netherlands)</li>
<li><a href="/wiki/H._Rider_Haggard" title="H. Rider Haggard">H. Rider Haggard</a> (1856–1925, England)</li>
<li><a href="/wiki/Barbara_Hambly" title="Barbara Hambly">Barbara Hambly</a> (born 1951, US)</li>
<li><a href="/wiki/Judith_Hand" title="Judith Hand">Judith Hand</a> (born 1940, US)</li>
<li><a href="/wiki/Enrica_von_Handel-Mazzetti" title="Enrica von Handel-Mazzetti">Enrica von Handel-Mazzetti</a> (1871–1955, Austria)</li>
<li><a href="/wiki/Kristin_Hannah" title="Kristin Hannah">Kristin Hannah</a> (born 1960, US)</li>
<li><a href="/wiki/Paul_C._Doherty" title="Paul C. Doherty">Paul Harding</a> (born 1946, England)</li>
<li><a href="/wiki/Paul_C._Doherty" title="Paul C. Doherty">Mollie Hardwick</a> (born 1946, England)</li>
<li><a href="/wiki/Thomas_Hardy" title="Thomas Hardy">Thomas Hardy</a> (1840–1928, England)</li>
<li><a href="/wiki/Cynthia_Harnett" title="Cynthia Harnett">Cynthia Harnett</a> (1893–1981, England)</li>
<li><a href="/wiki/Stephen_Harrigan" title="Stephen Harrigan">Stephen Harrigan</a> (born 1948, US)</li>
<li><a href="/wiki/Robert_Harris_(novelist)" title="Robert Harris (novelist)">Robert Harris</a> (born 1957, England)</li>
<li><a href="/wiki/Christopher_Hart_(novelist)" title="Christopher Hart (novelist)">Christopher Hart</a> (born 1965, England), pseudonym William Napier</li>
<li><a href="/wiki/Sonya_Hartnett" title="Sonya Hartnett">Sonya Hartnett</a> (born 1968, Australia)</li>
<li><a href="/wiki/Samantha_Harvey_(author)" title="Samantha Harvey (author)">Samantha Harvey</a> (born 1975, England)</li>
<li><a href="/wiki/Charles_Boardman_Hawes" title="Charles Boardman Hawes">Charles Boardman Hawes</a> (1889–1923, US)</li>
<li><a href="/wiki/Simon_Hawke" title="Simon Hawke">Simon Hawke</a> (born 1951, US)</li>
<li><a href="/wiki/Karen_Hawkins_(author)" title="Karen Hawkins (author)">Karen Hawkins</a> (living, US)</li>
<li><a href="/wiki/Shirl_Henke" title="Shirl Henke">Shirl Henke</a> (born 1942, US)</li>
<li><a href="/wiki/Virginia_Henley" title="Virginia Henley">Virginia Henley</a> (born 1935, England)</li>
<li><a href="/wiki/Vera_Henriksen" title="Vera Henriksen">Vera Henriksen</a> (1927–2016, Norway)</li>
<li><a href="/wiki/G._A._Henty" title="G. A. Henty">G. A. Henty</a> (1832–1902, England)</li>
<li><a href="/wiki/Ferenc_Herczeg" title="Ferenc Herczeg">Ferenc Herczeg</a> (1863–1954, Hungary)</li>
<li><a href="/wiki/Maurice_Hewlett" title="Maurice Hewlett">Maurice Hewlett</a> (1861–1923, England)</li>
<li><a href="/wiki/Georgette_Heyer" title="Georgette Heyer">Georgette Heyer</a> (1902–1974, England)</li>
<li><a href="/wiki/Eleanor_Hibbert" title="Eleanor Hibbert">Eleanor Hibbert</a> (1906–1993, England)</li>
<li><a href="/wiki/Susan_Higginbotham" title="Susan Higginbotham">Susan Higginbotham</a> (living, US)</li>
<li><a href="/wiki/Justin_Hill_(writer)" title="Justin Hill (writer)">Justin Hill</a> (born 1971, Bahamas/Hong Kong)</li>
<li><a href="/wiki/Gin%C3%A9s_P%C3%A9rez_de_Hita" title="Ginés Pérez de Hita">Ginés Pérez de Hita</a> (c. 1544 – c. 1619, Spain)</li>
<li><a href="/wiki/Jane_Aiken_Hodge" title="Jane Aiken Hodge">Jane Aiken Hodge</a> (1917–2009, England)</li>
<li><a href="/wiki/C._Walter_Hodges" title="C. Walter Hodges">C. Walter Hodges</a> (1909–2004, England)</li>
<li><a href="/wiki/Tom_Holland_(author)" title="Tom Holland (author)">Tom Holland</a> (born 1968, England)</li>
<li><a href="/wiki/Sheri_Holman" title="Sheri Holman">Sheri Holman</a> (born 1966, US)</li>
<li><a href="/wiki/Emily_Sarah_Holt" title="Emily Sarah Holt">Emily Sarah Holt</a> (1836–1893, England)</li>
<li><a href="/wiki/Tom_Holt" title="Tom Holt">Tom Holt</a> (born 1961, England)</li>
<li><a href="/wiki/Eleanor_Hibbert" title="Eleanor Hibbert">Victoria Holt</a> (1906–1993, England)</li>
<li><a href="/wiki/Nancy_Horan" title="Nancy Horan">Nancy Horan</a> (living, US)</li>
<li><a href="/wiki/Hannah_Howell" title="Hannah Howell">Hannah Howell</a> (born 1950, US)</li>
<li><a href="/wiki/Elizabeth_Hoyt" title="Elizabeth Hoyt">Elizabeth Hoyt</a> (Julia Harper, living, US)</li>
<li><a href="/wiki/Victor_Hugo" title="Victor Hugo">Victor Hugo</a> (1802–1885, France)</li>
<li><a href="/wiki/Wilhelm_H%C3%BCnermann" title="Wilhelm Hünermann">Wilhelm Hünermann</a> (1900–1975, Germany)</li>
<li><a href="/wiki/Jillian_Hunter" title="Jillian Hunter">Jillian Hunter</a> (born 1950, US)</li>
<li><a href="/wiki/Nicholas_Yermakov" class="mw-redirect" title="Nicholas Yermakov">S. L. Hunter</a> (born 1951, US)</li></ul></div>
<h2><span class="mw-headline" id="I">I</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=List_of_historical_novelists&amp;action=edit&amp;section=9" title="Edit section: I">edit</a><span class="mw-editsection-bracket">]</span></span></h2>
<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r998391716"><div class="div-col" style="column-width: 20em;">
<ul><li><a href="/wiki/Eva_Ibbotson" title="Eva Ibbotson">Eva Ibbotson</a> (1925–2010, Austria/England)</li>
<li><a href="/wiki/Conn_Iggulden" title="Conn Iggulden">Conn Iggulden</a> (born 1971, England)</li>
<li><a href="/wiki/Sh%C5%8Dtar%C5%8D_Ikenami" title="Shōtarō Ikenami">Shōtarō Ikenami</a> (池波正太郎, 1923–1990, Japan)</li>
<li><a href="/wiki/Neamat_Imam" title="Neamat Imam">Neamat Imam</a> (born 1971, Bangladesh/Canada)</li>
<li><a href="/wiki/Elisabeth_Inglis-Jones" title="Elisabeth Inglis-Jones">Elisabeth Inglis-Jones</a> (1900–1994, Wales)</li>
<li><a href="/wiki/Yasushi_Inoue" title="Yasushi Inoue">Yasushi Inoue</a> (born 1907, Japan)</li>
<li><a href="/wiki/Kazuo_Ishiguro" title="Kazuo Ishiguro">Kazuo Ishiguro</a> (born 1954, Japan/England)</li>
<li><a href="/wiki/Ismail_Fatah_Al_Turk" title="Ismail Fatah Al Turk">Ismail Fatah Al Turk</a> (1934 or 1938–2004, إسماعيل فتاح الترك, Iraq)</li>
<li><a href="/wiki/Eowyn_Ivey" title="Eowyn Ivey">Eowyn Ivey</a> (living, US)</li>
<li><a href="/wiki/Motohiko_Izawa" title="Motohiko Izawa">Motohiko Izawa</a> (born 1954, Japan)</li></ul></div>
<h2><span class="mw-headline" id="J">J</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=List_of_historical_novelists&amp;action=edit&amp;section=10" title="Edit section: J">edit</a><span class="mw-editsection-bracket">]</span></span></h2>
<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r998391716"><div class="div-col" style="column-width: 20em;">
<ul><li><a href="/wiki/Violet_Jacob" title="Violet Jacob">Violet Jacob</a> (1863–1946, Scotland)</li>
<li><a href="/wiki/Christian_Jacq" title="Christian Jacq">Christian Jacq</a> (born 1947, France)</li>
<li><a href="/wiki/John_Jakes" title="John Jakes">John Jakes</a> (born 1932, US)</li>
<li><a href="/wiki/George_Payne_Rainsford_James" title="George Payne Rainsford James">George Payne Rainsford James</a> (1799–1860, England)</li>
<li><a href="/wiki/Rosemary_Hawley_Jarman" title="Rosemary Hawley Jarman">Rosemary Hawley Jarman</a> (1935–2015, England)</li>
<li><a href="/wiki/Michael_Jecks" title="Michael Jecks">Michael Jecks</a> (born 1960, England)</li>
<li><a href="/wiki/Gary_Jennings_(author)" title="Gary Jennings (author)">Gary Jennings</a> (1928–1999, US)</li>
<li><a href="/wiki/John_Edward_Jennings" title="John Edward Jennings">John Edward Jennings</a> (1906–1973, US)</li>
<li><a href="/wiki/Alois_Jir%C3%A1sek" title="Alois Jirásek">Alois Jirásek</a> (1851–1930, Austrian Empire/Czechoslovakia)</li>
<li><a href="/wiki/Marie-Elena_John" title="Marie-Elena John">Marie-Elena John</a> (born 1963, Antigua/US)</li>
<li><a href="/wiki/Joan_Johnston" title="Joan Johnston">Joan Johnston</a> (living, US)</li>
<li><a href="/wiki/Rhiannon_Davies_Jones" title="Rhiannon Davies Jones">Rhiannon Davies Jones</a> (1921–2014, Wales)</li>
<li><a href="/wiki/T._Llew_Jones" title="T. Llew Jones">T. Llew Jones</a> (1915–2009, Wales)</li>
<li><a href="/wiki/Terry_Jones" title="Terry Jones">Terry Jones</a> (1942–2020, Wales)</li>
<li><a href="/wiki/Erica_Jong" title="Erica Jong">Erica Jong</a> (born 1942, US)</li>
<li><a href="/wiki/Penny_Jordan" title="Penny Jordan">Penny Jordan</a> (1946–2001, England)</li>
<li><a href="/wiki/Sherryl_Jordan" title="Sherryl Jordan">Sherryl Jordan</a> (born 1949, New Zealand)</li>
<li><a href="/wiki/Jacqueline_Jules" title="Jacqueline Jules">Jacqueline Jules</a> (born 1956, US)</li></ul></div>
<h2><span class="mw-headline" id="K">K</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=List_of_historical_novelists&amp;action=edit&amp;section=11" title="Edit section: K">edit</a><span class="mw-editsection-bracket">]</span></span></h2>
<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r998391716"><div class="div-col" style="column-width: 20em;">
<ul><li><a href="/wiki/Sirpa_K%C3%A4hk%C3%B6nen" title="Sirpa Kähkönen">Sirpa Kähkönen</a> (born 1964, Finland)</li>
<li><a href="/wiki/Ch%C5%8Dgor%C5%8D_Kaionji" title="Chōgorō Kaionji">Chōgorō Kaionji</a> (海音寺潮五郎, 1901–1977, Japan)</li>
<li><a href="/wiki/Amita_Kanekar" title="Amita Kanekar">Amita Kanekar</a> (born 1965, India)</li>
<li><a href="/wiki/John_Katzenbach" title="John Katzenbach">John Katzenbach</a> (born 1950, US)</li>
<li><a href="/wiki/Karen_Kay" title="Karen Kay">Karen Kay</a> (living, US)</li>
<li><a href="/wiki/Annie_Keary" title="Annie Keary">Annie Keary</a> (1825–1879, England)</li>
<li><a href="/wiki/Eleanor_Hibbert" title="Eleanor Hibbert">Kathleen Kellow</a> (1906–1993, England)</li>
<li><a href="/wiki/Carla_Kelly" title="Carla Kelly">Carla Kelly</a> (born 1947, US)</li>
<li><a href="/wiki/Sheelagh_Kelly" title="Sheelagh Kelly">Sheelagh Kelly</a> (born 1948, England)</li>
<li><a href="/wiki/Debra_Kemp" class="mw-redirect" title="Debra Kemp">Debra Kemp</a> (1957–2015, US)</li>
<li><a href="/wiki/Lena_Kennedy" title="Lena Kennedy">Lena Kennedy</a> (1914–1986, England)</li>
<li><a href="/wiki/Douglas_Reeman" title="Douglas Reeman">Alexander Kent</a> (1924–2017, England)</li>
<li><a href="/wiki/Louise_Andrews_Kent" title="Louise Andrews Kent">Louise Andrews Kent</a> (1886–1969, US)</li>
<li><a href="/wiki/Philip_Kerr" title="Philip Kerr">Philip Kerr</a> (1956–2018, England)</li>
<li><a href="/wiki/Sue_Monk_Kidd" title="Sue Monk Kidd">Sue Monk Kidd</a> (born 1948, US)</li>
<li><a href="/wiki/Garry_Kilworth" title="Garry Kilworth">Garry Kilworth</a> (born 1941, England)</li>
<li><a href="/wiki/Susan_King_(novelist)" title="Susan King (novelist)">Susan King</a> (born 1951, US)</li>
<li><a href="/wiki/Charles_Kingsley" title="Charles Kingsley">Charles Kingsley</a> (1819–1875, England)</li>
<li><a href="/wiki/Barbara_Kingsolver" title="Barbara Kingsolver">Barbara Kingsolver</a> (born 1955, US)</li>
<li><a href="/wiki/Rudyard_Kipling" title="Rudyard Kipling">Rudyard Kipling</a> (1865–1936, India/England)</li>
<li><a href="/wiki/Nobori_Kiuchi" title="Nobori Kiuchi">Nobori Kiuchi</a> (木内昇, b. 1967, Japan)</li>
<li><a href="/wiki/Julie_Klassen" title="Julie Klassen">Julie Klassen</a> (living, US)</li>
<li><a href="/wiki/Lisa_Kleypas" title="Lisa Kleypas">Lisa Kleypas</a> (born 1964, US)</li>
<li><a href="/wiki/Bernard_Knight" title="Bernard Knight">Bernard Knight</a> (born 1931, Wales/England)</li>
<li><a href="/wiki/Arthur_Koestler" title="Arthur Koestler">Arthur Koestler</a> (1905–1983, Hungary/England)</li>
<li><a href="/wiki/E._L._Konigsburg" title="E. L. Konigsburg">E. L. Konigsburg</a> (1930–2013, US)</li>
<li><a href="/wiki/Zofia_Kossak-Szczucka" title="Zofia Kossak-Szczucka">Zofia Kossak-Szczucka</a> (1889–1968, Poland)</li>
<li><a href="/wiki/Marek_Krajewski" title="Marek Krajewski">Marek Krajewski</a> (born 1966, Poland)</li>
<li><a href="/wiki/J%C3%B3zef_Ignacy_Kraszewski" title="Józef Ignacy Kraszewski">Józef Ignacy Kraszewski</a> (1812–1887, Poland)</li>
<li><a href="/wiki/Kalki_Krishnamurthy" title="Kalki Krishnamurthy">Kalki Krishnamurthy</a> (1899–1954, India)</li>
<li><a href="/wiki/Giles_Kristian" title="Giles Kristian">Giles Kristian</a> (born 1975, England))</li>
<li><a href="/wiki/Jaan_Kross" title="Jaan Kross">Jaan Kross</a> (1920–2007, Estonia)</li>
<li><a href="/wiki/Gyula_Kr%C3%BAdy" title="Gyula Krúdy">Gyula Krúdy</a> (1878–1933, Hungary)</li>
<li><a href="/wiki/Lynn_Kurland" title="Lynn Kurland">Lynn Kurland</a> (living, US)</li>
<li><a href="/wiki/Katherine_Kurtz" title="Katherine Kurtz">Katherine Kurtz</a> (born 1944, US)</li>
<li><a href="/wiki/Hermann_Kurz" title="Hermann Kurz">Hermann Kurz</a> (1813–1873, Germany)</li></ul></div>
<h2><span class="mw-headline" id="L">L</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=List_of_historical_novelists&amp;action=edit&amp;section=12" title="Edit section: L">edit</a><span class="mw-editsection-bracket">]</span></span></h2>
<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r998391716"><div class="div-col" style="column-width: 20em;">
<ul><li><a href="/wiki/R._A._Lafferty" title="R. A. Lafferty">R. A. Lafferty</a> (1914–2002, US)</li>
<li><a href="/wiki/Ross_Laidlaw_(author)" title="Ross Laidlaw (author)">Ross Laidlaw</a> (living, Scotland)</li>
<li><a href="/wiki/Elizabeth_Laird_(author)" title="Elizabeth Laird (author)">Elizabeth Laird</a> (born 1943, England)</li>
<li><a href="/wiki/Ludwig_Laistner" title="Ludwig Laistner">Ludwig Laistner</a> (1845–1896, Germany)</li>
<li><a href="/wiki/Giuseppe_Tomasi_di_Lampedusa" title="Giuseppe Tomasi di Lampedusa">Giuseppe Tomasi di Lampedusa</a> (1896–1957, Italy)</li>
<li><a href="/wiki/Jill_Marie_Landis" title="Jill Marie Landis">Jill Marie Landis</a> (born 1948, US)</li>
<li><a href="/wiki/Jane_Lane_(author)" title="Jane Lane (author)">Jane Lane</a> (1905–1978, England)</li>
<li><a href="/wiki/Andrew_Lang" title="Andrew Lang">Andrew Lang</a> (1844–1912, Scotland/England)</li>
<li><a href="/wiki/W._Patrick_Lang" title="W. Patrick Lang">W. Patrick Lang</a> (born 1940, US)</li>
<li><a href="/wiki/Noel_Langley" title="Noel Langley">Noel Langley</a> (1911–1980, South Africa/US)</li>
<li><a href="/wiki/Jane_Langton" title="Jane Langton">Jane Langton</a> (1922–2018, US)</li>
<li><a href="/wiki/Mariano_Jos%C3%A9_de_Larra" title="Mariano José de Larra">Mariano José de Larra</a> (1809–1837, Spain)</li>
<li><a href="/wiki/David_Lassman" class="mw-redirect" title="David Lassman">David Lassman</a> (born 1963, England)</li>
<li><a href="/wiki/Janet_Laurence_(author)" title="Janet Laurence (author)">Janet Laurence</a> (born 1937, England)</li>
<li><a href="/wiki/Stephen_R._Lawhead" title="Stephen R. Lawhead">Stephen R. Lawhead</a> (born 1950, US/England)</li>
<li><a href="/wiki/Halld%C3%B3r_Laxness" title="Halldór Laxness">Halldór Laxness</a> (1902–1998, Iceland)</li>
<li><a href="/wiki/Sophia_Lee" title="Sophia Lee">Sophia Lee</a> (1750–1824, England)</li>
<li><a href="/wiki/George_Leonardos" title="George Leonardos">George Leonardos</a> (born 1937, Greece)</li>
<li><a href="/wiki/Perry_Lentz" title="Perry Lentz">Perry Lentz</a> (born 1943, US)</li>
<li><a href="/wiki/Doris_Leslie" title="Doris Leslie">Doris Leslie</a> (1891–1982, England)</li>
<li><a href="/wiki/Celia_Moss_Levetus" title="Celia Moss Levetus">Celia Moss Levetus</a> (1819–1873, England)</li>
<li><a href="/wiki/Hilda_Lewis" title="Hilda Lewis">Hilda Lewis</a> (1896–1974, England)</li>
<li><a href="/wiki/Stephen_Lewis" title="Stephen Lewis">Stephen Lewis</a> (born 1937, Canada)</li>
<li><a href="/wiki/Philip_Lindsay" title="Philip Lindsay">Philip Lindsay</a> (1906–1958, Australia)</li>
<li><a href="/wiki/Johanna_Lindsey" title="Johanna Lindsey">Johanna Lindsey</a> (1952–2019, US)</li>
<li><a href="/wiki/Ling_Li_(writer)" title="Ling Li (writer)">Ling Li</a> (曾黎力, 1942–2018, China)</li>
<li><a href="/wiki/David_Liss" title="David Liss">David Liss</a> (born 1966, US)</li>
<li><a href="/wiki/S._E._Lister" title="S. E. Lister">S. E. Lister</a> (born 1988, England)</li>
<li><a href="/wiki/Penelope_Lively" title="Penelope Lively">Penelope Lively</a> (born 1933, England)</li>
<li><a href="/wiki/John_Gibson_Lockhart" title="John Gibson Lockhart">John Gibson Lockhart</a> (1794–1854, Scotland)</li>
<li><a href="/wiki/Christoph_Lode" title="Christoph Lode">Christoph Lode</a> (born 1977, Germany)</li>
<li><a href="/wiki/William_Stuart_Long" class="mw-redirect" title="William Stuart Long">William Stuart Long</a> (1914–1986, England)</li>
<li><a href="/wiki/Norah_Lofts" title="Norah Lofts">Norah Lofts</a> (1904–1983, England)</li>
<li><a href="/wiki/Jarmila_Loukotkov%C3%A1" title="Jarmila Loukotková">Jarmila Loukotková</a> (1923–2007, Czechoslovakia/Czech Republic)</li>
<li><a href="/wiki/Luo_Guanzhong" title="Luo Guanzhong">Luo Guanzhong</a> (1330–1400, China)</li></ul></div>
<h2><span class="mw-headline" id="M">M</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=List_of_historical_novelists&amp;action=edit&amp;section=13" title="Edit section: M">edit</a><span class="mw-editsection-bracket">]</span></span></h2>
<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r998391716"><div class="div-col" style="column-width: 20em;">
<ul><li><a href="/wiki/Ma_Duanlin" title="Ma Duanlin">Ma Duanlin</a> (1245–1322, China)</li>
<li><a href="/wiki/Catherine_Maberly" title="Catherine Maberly">Catherine Maberly</a> (1805–1875, Ireland)</li>
<li><a href="/wiki/Rose_Macaulay" title="Rose Macaulay">Rose Macaulay</a> (1881–1958, England)</li>
<li><a href="/wiki/Mary_Mackie" title="Mary Mackie">Mary Mackie</a> (born early 1940s, England)</li>
<li><a href="/wiki/Salvador_de_Madariaga" title="Salvador de Madariaga">Salvador de Madariaga</a> (1886–1978, Spain)</li>
<li><a href="/wiki/Ragnhild_Mager%C3%B8y" title="Ragnhild Magerøy">Ragnhild Magerøy</a> (1920–2010, Norway)</li>
<li><a href="/wiki/Naguib_Mahfouz" title="Naguib Mahfouz">Naguib Mahfouz</a> (1911–2006, Egypt)</li>
<li><a href="/wiki/Karen_Maitland" title="Karen Maitland">Karen Maitland</a> (born 1956, England)</li>
<li><a href="/wiki/Eduardo_Mendoza_Garriga" title="Eduardo Mendoza Garriga">Eduardo Mendoza</a> (born 1943, Spain)</li>
<li><a href="/wiki/Paul_L._Maier" title="Paul L. Maier">Paul L. Maier</a> (born 1930, US)</li>
<li><a href="/wiki/Rosie_Malek-Yonan" title="Rosie Malek-Yonan">Rosie Malek-Yonan</a> (born 1965, Iran/US)</li>
<li><a href="/wiki/Thomas_Mallon" title="Thomas Mallon">Thomas Mallon</a> (born 1951, US)</li>
<li><a href="/wiki/Eric_Malpass" title="Eric Malpass">Eric Malpass</a> (1910–1996, England)</li>
<li><a href="/wiki/Heinrich_Mann" title="Heinrich Mann">Heinrich Mann</a> (1871–1950, Germany/France)</li>
<li><a href="/wiki/Thomas_Mann" title="Thomas Mann">Thomas Mann</a> (1875–1955, Germany/Switzerland)</li>
<li><a href="/wiki/Anne_Manning_(novelist)" title="Anne Manning (novelist)">Anne Manning</a> (1807–1879, England)</li>
<li><a href="/wiki/Hilary_Mantel" title="Hilary Mantel">Hilary Mantel</a> (born 1952, England)</li>
<li><a href="/wiki/Valerio_Massimo_Manfredi" title="Valerio Massimo Manfredi">Valerio Massimo Manfredi</a> (born 1942, Italy)</li>
<li><a href="/wiki/Stephen_Marley_(writer)" title="Stephen Marley (writer)">Stephen Marley</a> (living, England)</li>
<li><a href="/wiki/Deb_Marlowe" title="Deb Marlowe">Deb Marlowe</a> (living, US)</li>
<li><a href="/wiki/Paul_Marlowe" title="Paul Marlowe">Paul Marlowe</a> (living, Canada)</li>
<li><a href="/wiki/Andrew_Martin_(novelist)" title="Andrew Martin (novelist)">Andrew Martin</a> (born 1962, England)</li>
<li><a href="/wiki/Valerie_Martin" title="Valerie Martin">Valerie Martin</a> (born 1948, US)</li>
<li><a href="/wiki/Moa_Martinson" title="Moa Martinson">Moa Martinson</a> (1890–1964, Sweden)</li>
<li><a href="/wiki/F._Van_Wyck_Mason" title="F. Van Wyck Mason">F. Van Wyck Mason</a> (1901–1978, US)</li>
<li><a href="/wiki/Simon_Hawke" title="Simon Hawke">J. D. Masters</a> (born 1951, US)</li>
<li><a href="/wiki/John_Masters" title="John Masters">John Masters</a> (1914–1983, India)</li>
<li><a href="/wiki/Seich%C5%8D_Matsumoto" title="Seichō Matsumoto">Seichō Matsumoto</a> (松本清張, 1909–1992, Japan)</li>
<li><a href="/wiki/Ellen_Mattson" title="Ellen Mattson">Ellen Mattson</a> (b. 1962, Sweden)</li>
<li><a href="/wiki/Sir_Herbert_Maxwell,_7th_Baronet" title="Sir Herbert Maxwell, 7th Baronet">Sir Herbert Maxwell</a> (1845–1937, Scotland)</li>
<li><a href="/wiki/William_Mayne" title="William Mayne">William Mayne</a> (1928–2010, England)</li>
<li><a href="/wiki/Cormac_McCarthy" title="Cormac McCarthy">Cormac McCarthy</a> (born 1933, US)</li>
<li><a href="/wiki/Colleen_McCullough" title="Colleen McCullough">Colleen McCullough</a> (born 1937, Australia)</li>
<li><a href="/wiki/Ian_McEwan" title="Ian McEwan">Ian McEwan</a> (born 1948, England)</li>
<li><a href="/wiki/Katharine_McMahon" title="Katharine McMahon">Katharine McMahon</a> (living, England)</li>
<li><a href="/wiki/Larry_McMurtry" title="Larry McMurtry">Larry McMurtry</a> (1936–2021, US)</li>
<li><a href="/wiki/James_Meek_(author)" title="James Meek (author)">James Meek</a> (born 1962, England)</li>
<li><a href="/wiki/Elizabeth_Meeke" title="Elizabeth Meeke">Elizabeth Meeke</a> (1761 – c. 1826, England)</li>
<li><a href="/wiki/Wilhelm_Meinhold" title="Wilhelm Meinhold">Wilhelm Meinhold</a> (1797–1851, Pomerania/Germany)</li>
<li><a href="/wiki/Dmitry_Merezhkovsky" title="Dmitry Merezhkovsky">Dmitry Merezhkovsky</a> (1865–1941, Russia/France)</li>
<li><a href="/wiki/Robert_Merle" title="Robert Merle">Robert Merle</a> (1908–2004, France)</li>
<li><a href="/wiki/Conrad_Ferdinand_Meyer" title="Conrad Ferdinand Meyer">Conrad Ferdinand Meyer</a> (1825–1898, Switzerland)</li>
<li><a href="/wiki/James_A._Michener" title="James A. Michener">James A. Michener</a> (1907–1997, US)</li>
<li><a href="/wiki/K%C3%A1lm%C3%A1n_Miksz%C3%A1th" title="Kálmán Mikszáth">Kálmán Mikszáth</a> (1847–1940, Hungary)</li>
<li><a href="/wiki/Andrew_Miller_(novelist)" title="Andrew Miller (novelist)">Andrew Miller</a> (born 1960, England)</li>
<li><a href="/wiki/Linda_Lael_Miller" title="Linda Lael Miller">Linda Lael Miller</a> (born 1949, US)</li>
<li><a href="/wiki/Madeline_Miller" title="Madeline Miller">Madeline Miller</a> (born 1978, US)</li>
<li><a href="/wiki/David_Mitchell_(author)" title="David Mitchell (author)">David Mitchell</a> (born 1969, England)</li>
<li><a href="/wiki/Margaret_Mitchell" title="Margaret Mitchell">Margaret Mitchell</a> (1900–1949, US)</li>
<li><a href="/wiki/Naomi_Mitchison" title="Naomi Mitchison">Naomi Mitchison</a> (1897–1999, Scotland/England)</li>
<li><a href="/wiki/Ryu_Mitsuse" title="Ryu Mitsuse">Ryu Mitsuse</a> (光瀬龍, 1928–1999, Japan)</li>
<li><a href="/wiki/Karyn_Monk" title="Karyn Monk">Karyn Monk</a> (living, Canada)</li>
<li><a href="/wiki/Ferenc_M%C3%B3ra" title="Ferenc Móra">Ferenc Móra</a> (1879–1934, Hungary)</li>
<li><a href="/wiki/Brian_Moore_(novelist)" title="Brian Moore (novelist)">Brian Moore</a> (1921–1999, N. Ireland/US)</li>
<li><a href="/wiki/Thomas_Moore" title="Thomas Moore">Thomas Moore</a> (1779–1852, Ireland/England)</li>
<li><a href="/wiki/Michelle_Moran" title="Michelle Moran">Michelle Moran</a> (born 1980, US)</li>
<li><a href="/wiki/Daniil_Mordovtsev" title="Daniil Mordovtsev">Daniil Mordovtsev</a> (1830–1905, Russia)</li>
<li><a href="/wiki/Toni_Morrison" title="Toni Morrison">Toni Morrison</a> (1931–2019, US)</li>
<li><a href="/wiki/Kate_Morton" title="Kate Morton">Kate Morton</a> (born 1976, Australia)</li>
<li><a href="/wiki/Fiona_Mozley" title="Fiona Mozley">Fiona Mozley</a> (born 1988, England)</li>
<li><a href="/wiki/Luise_M%C3%BChlbach" title="Luise Mühlbach">Luise Mühlbach</a> (1814–1873, Germany)</li>
<li><a href="/wiki/Vera_Mutafchieva" title="Vera Mutafchieva">Vera Mutafchieva</a> (1929–2009, Bulgaria)</li></ul></div>
<h2><span class="mw-headline" id="N">N</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=List_of_historical_novelists&amp;action=edit&amp;section=14" title="Edit section: N">edit</a><span class="mw-editsection-bracket">]</span></span></h2>
<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r998391716"><div class="div-col" style="column-width: 20em;">
<ul><li><a href="/wiki/Ladislav_N%C3%A1da%C5%A1i-J%C3%A9g%C3%A9" title="Ladislav Nádaši-Jégé">Ladislav Nádaši-Jégé</a> (1866–1940, Hungary/Czechoslovakia)</li>
<li><a href="/wiki/Michiko_Nagai" title="Michiko Nagai">Michiko Nagai</a> (born 1925, Japan)</li>
<li><a href="/wiki/Naseem_Hijazi" title="Naseem Hijazi">Naseem Hijazi</a> (born 1914, India/Pakistan)</li>
<li><a href="/wiki/Marie_von_Najmajer" title="Marie von Najmajer">Marie von Najmajer</a> (1844–1904, Austrian E)</li>
<li><a href="/wiki/Benedikte_Naubert" title="Benedikte Naubert">Benedikte Naubert</a> (1752–1819, Germany)</li>
<li><a href="/wiki/John_Neal_(writer)" title="John Neal (writer)">John Neal</a> (1793–1876, US)</li>
<li><a href="/wiki/Vladim%C3%ADr_Neff" title="Vladimír Neff">Vladimír Neff</a> (1909–1983, Czechoslovakia)</li>
<li><a href="/wiki/John_Henry_Newman" title="John Henry Newman">John Henry Newman</a> (1801–1890, England)</li>
<li><a href="/wiki/Nerida_Newton" title="Nerida Newton">Nerida Newton</a> (born 1972, Australia)</li>
<li><a href="/wiki/Nicholas_Nicastro" title="Nicholas Nicastro">Nicholas Nicastro</a> (born 1963, US)</li>
<li><a href="/wiki/Luis_L%C3%B3pez_Nieves" title="Luis López Nieves">Luis López Nieves</a> (born 1950, Puerto Rico)</li>
<li><a href="/wiki/Jir%C5%8D_Nitta" title="Jirō Nitta">Jirō Nitta</a> (1912–1980, Japan)</li>
<li><a href="/wiki/Jennifer_Niven" title="Jennifer Niven">Jennifer Niven</a> (born 1968, US)</li>
<li><a href="/wiki/Andre_Norton" title="Andre Norton">Andre Norton</a> (1912–2005, US)</li>
<li><a href="/wiki/Mary_Novik" title="Mary Novik">Mary Novik</a> (born 1945, Canada)</li>
<li><a href="/wiki/Robert_Nye" title="Robert Nye">Robert Nye</a> (born 1939, England)</li></ul></div>
<h2><span class="mw-headline" id="O">O</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=List_of_historical_novelists&amp;action=edit&amp;section=15" title="Edit section: O">edit</a><span class="mw-editsection-bracket">]</span></span></h2>
<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r998391716"><div class="div-col" style="column-width: 20em;">
<ul><li><a href="/wiki/Patrick_O%27Brian" title="Patrick O'Brian">Patrick O'Brian</a> (1914–2000, England)</li>
<li><a href="/wiki/Scott_O%27Dell" title="Scott O'Dell">Scott O'Dell</a> (1898–1989, US)</li>
<li><a href="/wiki/Scott_Oden" title="Scott Oden">Scott Oden</a> (born 1967, US)</li>
<li><a href="/wiki/Zoe_Oldenbourg" class="mw-redirect" title="Zoe Oldenbourg">Zoe Oldenbourg</a> (1916–2002, France)</li>
<li><a href="/wiki/Margaret_Oliphant" title="Margaret Oliphant">Margaret Oliphant</a> (1828–1897, Scotland/England)</li>
<li><a href="/wiki/Carola_Oman" title="Carola Oman">Carola Oman</a> (1897–1978, England)</li>
<li><a href="/wiki/Michael_Ondaatje" title="Michael Ondaatje">Michael Ondaatje</a> (born 1943, Canada)</li>
<li><a href="/wiki/Anthony_O%27Neill" title="Anthony O'Neill">Anthony O'Neill</a> (born 1964, Australia)</li>
<li><a href="/wiki/Geraldine_O%27Neill" title="Geraldine O'Neill">Geraldine O'Neill</a> (born 1955, Ireland)</li>
<li><a href="/wiki/Emma_Orczy" class="mw-redirect" title="Emma Orczy">Baroness Orczy</a> (1865–1947, England)</li>
<li><a href="/wiki/Julie_Orringer" title="Julie Orringer">Julie Orringer</a> (born 1973, US)</li></ul></div>
<h2><span class="mw-headline" id="P">P</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=List_of_historical_novelists&amp;action=edit&amp;section=16" title="Edit section: P">edit</a><span class="mw-editsection-bracket">]</span></span></h2>
<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r998391716"><div class="div-col" style="column-width: 20em;">
<ul><li><a href="/wiki/Henriette_Paalzow" title="Henriette Paalzow">Henriette Paalzow</a> (1788–1847, Germany)</li>
<li><a href="/wiki/Charles_Palliser" title="Charles Palliser">Charles Palliser</a> (born 1947, US/Scotland)</li>
<li><a href="/wiki/William_Palmer_(novelist)" title="William Palmer (novelist)">William Palmer</a> (born 1943, US)</li>
<li><a href="/wiki/Jan_Parandowski" title="Jan Parandowski">Jan Parandowski</a> (1895–1978, Poland)</li>
<li><a href="/wiki/Edith_Pargeter" title="Edith Pargeter">Edith Pargeter</a> (1913–1995, England)</li>
<li><a href="/wiki/Delia_Parr" title="Delia Parr">Delia Parr</a> (living, US)</li>
<li><a href="/wiki/Walter_Pater" title="Walter Pater">Walter Pater</a> (1839–1894, England)</li>
<li><a href="/wiki/Jenny_Pattrick" title="Jenny Pattrick">Jenny Pattrick</a> (born 1936, New Zealand)</li>
<li><a href="/wiki/Frances_Mary_Peard" title="Frances Mary Peard">Frances Mary Peard</a> (1835–1923, England)</li>
<li><a href="/wiki/Iain_Pears" title="Iain Pears">Iain Pears</a> (born 1955, England)</li>
<li><a href="/wiki/Borislav_Peki%C4%87" title="Borislav Pekić">Borislav Pekić</a> (1930–1992, Yugoslavia)</li>
<li><a href="/wiki/Sharon_Kay_Penman" title="Sharon Kay Penman">Sharon Kay Penman</a> (born 1945, US)</li>
<li><a href="/wiki/Stef_Penney" title="Stef Penney">Stef Penney</a> (born 1969, Scotland)</li>
<li><a href="/wiki/Anna_Percival" class="mw-redirect" title="Anna Percival">Anna Percival</a> (1906–1993, England)</li>
<li><a href="/wiki/Eva_D%C3%ADaz_P%C3%A9rez" title="Eva Díaz Pérez">Eva Díaz Pérez</a> (born 1971, Spain)</li>
<li><a href="/wiki/Arturo_P%C3%A9rez-Reverte" title="Arturo Pérez-Reverte">Arturo Pérez-Reverte</a> (born 1951, Spain)</li>
<li><a href="/wiki/Anne_Perry" title="Anne Perry">Anne Perry</a> (born 1938, England)</li>
<li><a href="/wiki/Malte_Persson" title="Malte Persson">Malte Persson</a> (born 1976, Sweden)</li>
<li><a href="/wiki/Leo_Perutz" title="Leo Perutz">Leo Perutz</a> (1882–1957, Austria/Palestine)</li>
<li><a href="/wiki/Elizabeth_Peters" class="mw-redirect" title="Elizabeth Peters">Elizabeth Peters</a> (1927–2013, US)</li>
<li><a href="/wiki/Edith_Pargeter" title="Edith Pargeter">Ellis Peters</a> (1913–1995, England)</li>
<li><a href="/wiki/Maureen_Peters_(novelist)" title="Maureen Peters (novelist)">Maureen Peters</a> (1935–2008, Wales/England)</li>
<li><a href="/wiki/Karoline_Pichler" title="Karoline Pichler">Karoline Pichler</a> (1769–1843, Austria)</li>
<li><a href="/wiki/Jean_Plaidy" class="mw-redirect" title="Jean Plaidy">Jean Plaidy</a> (Eleanor Hibbert, 1906–1993, England)</li>
<li><a href="/wiki/Madeleine_A._Polland" title="Madeleine A. Polland">Madeleine A. Polland</a> (1918–2005, Ireland/England)</li>
<li><a href="/wiki/Dudley_Pope" title="Dudley Pope">Dudley Pope</a> (1925–1997, England)</li>
<li><a href="/wiki/Fani_Popova-Mutafova" title="Fani Popova-Mutafova">Fani Popova-Mutafova</a> (1902–1977, Bulgaria)</li>
<li><a href="/wiki/Jovan_Sterija_Popovi%C4%87" title="Jovan Sterija Popović">Jovan Sterija Popović</a> (1806–1856, Austrian E)</li>
<li><a href="/wiki/Jane_Porter" title="Jane Porter">Jane Porter</a> (1776–1850, Scotland/England)</li>
<li><a href="/wiki/Rhoda_Power" title="Rhoda Power">Rhoda Power</a> (1890–1957), England</li>
<li><a href="/wiki/H._F._M._Prescott" title="H. F. M. Prescott">H. F. M. Prescott</a> (1896–1972, England)</li>
<li><a href="/wiki/Steven_Pressfield" title="Steven Pressfield">Steven Pressfield</a> (born 1943, US)</li>
<li><a href="/wiki/Otfried_Preu%C3%9Fler" title="Otfried Preußler">Otfried Preußler</a> (1923–2013, Germany)</li>
<li><a href="/wiki/Alison_Prince" title="Alison Prince">Alison Prince</a> (1931–2019, England/Scotland)</li>
<li><a href="/wiki/Boles%C5%82aw_Prus" title="Bolesław Prus">Bolesław Prus</a> (1847–1912, Poland)</li>
<li><a href="/wiki/Alexander_Pushkin" title="Alexander Pushkin">Alexander Pushkin</a> (1799–1837, Russia)</li>
<li><a href="/wiki/Mary_Jo_Putney" title="Mary Jo Putney">Mary Jo Putney</a> (living, US)</li>
<li><a href="/wiki/Howard_Pyle" title="Howard Pyle">Howard Pyle</a> (1853–1911, US)</li>
<li><a href="/wiki/Thomas_Pynchon" title="Thomas Pynchon">Thomas Pynchon</a> (born 1937, US)</li></ul></div>
<h2><span class="mw-headline" id="Q">Q</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=List_of_historical_novelists&amp;action=edit&amp;section=17" title="Edit section: Q">edit</a><span class="mw-editsection-bracket">]</span></span></h2>
<ul><li><a href="/wiki/John_Quigley_(author)" title="John Quigley (author)">John Quigley</a> (born 1925, Scotland)</li></ul>
<h2><span class="mw-headline" id="R">R</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=List_of_historical_novelists&amp;action=edit&amp;section=18" title="Edit section: R">edit</a><span class="mw-editsection-bracket">]</span></span></h2>
<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r998391716"><div class="div-col" style="column-width: 20em;">
<ul><li><a href="/wiki/Thomas_Head_Raddall" title="Thomas Head Raddall">Thomas Head Raddall</a> (1903–1994, England/Canada)</li>
<li><a href="/wiki/Undin%C4%97_Radzevi%C4%8Di%C5%ABt%C4%97" title="Undinė Radzevičiūtė">Undinė Radzevičiūtė</a> (b. 1967, Lithuania)</li>
<li><a href="/wiki/Hugh_C._Rae" title="Hugh C. Rae">Hugh C. Rae</a> (1935–2014, Scotland)</li>
<li><a href="/wiki/William_Rayner" title="William Rayner">William Rayner</a> (1929–2006, England)</li>
<li><a href="/wiki/Charles_Reade" title="Charles Reade">Charles Reade</a> (1814–1884, England)</li>
<li><a href="/wiki/Jaclyn_Reding" title="Jaclyn Reding">Jaclyn Reding</a> (born 1966, US)</li>
<li><a href="/wiki/Douglas_Reeman" title="Douglas Reeman">Douglas Reeman</a> (1924–2017, England)</li>
<li><a href="/wiki/Celia_Rees" title="Celia Rees">Celia Rees</a> (b. 1949, England)</li>
<li><a href="/wiki/David_Rees_(author)" title="David Rees (author)">David Rees</a> (1936–1993, England)</li>
<li><a href="/wiki/Evan_Rees_(Dyfed)" title="Evan Rees (Dyfed)">Evan Rees</a> (Wales, p/nf)</li>
<li><a href="/wiki/Philip_Reeve" title="Philip Reeve">Philip Reeve</a> (born 1966, England)</li>
<li><a href="/wiki/Meta_Mayne_Reid" title="Meta Mayne Reid">Meta Mayne Reid</a> (1905–1991, Northern Ireland)</li>
<li><a href="/wiki/Franziska_von_Reitzenstein" title="Franziska von Reitzenstein">Franziska von Reitzenstein</a> (1834–1896, Germany)</li>
<li><a href="/wiki/Mary_Renault" title="Mary Renault">Mary Renault</a> (1905–1983, England)</li>
<li><a href="/wiki/Rick_Riordan" title="Rick Riordan">Rick Riordan</a> (born 1964, US)</li>
<li><a href="/wiki/Karl_Ristikivi" title="Karl Ristikivi">Karl Ristikivi</a> (1907–1970, Estonia)</li>
<li><a href="/wiki/Kel_Richards" title="Kel Richards">Kel Richards</a> (born 1946, Australia)</li>
<li><a href="/wiki/Candace_Robb" title="Candace Robb">Candace Robb</a> (born 1950, England/US)</li>
<li><a href="/wiki/Antoinette_Henriette_Cl%C3%A9mence_Robert" title="Antoinette Henriette Clémence Robert">Antoinette Henriette Clémence Robert</a> (1797–1872, France)</li>
<li><a href="/wiki/Keith_Roberts" title="Keith Roberts">Keith Roberts</a> (1935–2000, England)</li>
<li><a href="/wiki/Kenneth_Roberts_(author)" title="Kenneth Roberts (author)">Kenneth Roberts</a> (1885–1957, US)</li>
<li><a href="/wiki/Emma_Robinson_(author)" title="Emma Robinson (author)">Emma Robinson</a> (1814–1890, England)</li>
<li><a href="/wiki/Hilary_Robinson_(author)" title="Hilary Robinson (author)">Hilary Robinson</a> (born 1962, England)</li>
<li><a href="/wiki/Lynda_Robinson" class="mw-redirect" title="Lynda Robinson">Lynda Robinson</a> (born 1951, US)</li>
<li><a href="/wiki/Lucia_St._Clair_Robson" title="Lucia St. Clair Robson">Lucia St. Clair Robson</a> (born 1942, US)</li>
<li><a href="/wiki/Tsoncho_Rodev" title="Tsoncho Rodev">Tsoncho Rodev</a> (1926–2011, Bulgaria)</li>
<li><a href="/wiki/Rosemary_Rogers" title="Rosemary Rogers">Rosemary Rogers</a> (1932–2019, Ceylon/US)</li>
<li><a href="/wiki/Romain_Rolland" title="Romain Rolland">Romain Rolland</a> (1866–1944, France)</li>
<li><a href="/wiki/Elliott_Roosevelt" title="Elliott Roosevelt">Elliott Roosevelt</a> (1910–1990, US)</li>
<li><a href="/wiki/Tatiana_de_Rosnay" title="Tatiana de Rosnay">Tatiana de Rosnay</a> (born 1961, France/England)</li>
<li><a href="/wiki/Joseph_Roth" title="Joseph Roth">Joseph Roth</a> (1894–1939, Austria/Germany)</li>
<li><a href="/wiki/Laura_Joh_Rowland" title="Laura Joh Rowland">Laura Joh Rowland</a> (living, US)</li>
<li><a href="/wiki/Fredrika_Runeberg" title="Fredrika Runeberg">Fredrika Runeberg</a> (1807–1879, Finland)</li>
<li><a href="/wiki/Salman_Rushdie" title="Salman Rushdie">Salman Rushdie</a> (born 1947, England/US)</li>
<li><a href="/wiki/Mary_Doria_Russell" title="Mary Doria Russell">Mary Doria Russell</a> (born 1950, US)</li>
<li><a href="/wiki/Anna_Rutgers_van_der_Loeff" title="Anna Rutgers van der Loeff">Anna Rutgers van der Loeff</a> (1910–1990, Netherlands)</li>
<li><a href="/wiki/Edward_Rutherfurd" title="Edward Rutherfurd">Edward Rutherfurd</a> (born 1948, England)</li>
<li><a href="/wiki/Viktor_Rydberg" title="Viktor Rydberg">Viktor Rydberg</a> (1828–1895, Sweden)</li></ul></div>
<h2><span class="mw-headline" id="S">S</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=List_of_historical_novelists&amp;action=edit&amp;section=19" title="Edit section: S">edit</a><span class="mw-editsection-bracket">]</span></span></h2>
<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r998391716"><div class="div-col" style="column-width: 20em;">
<ul><li><a href="/wiki/Rafael_Sabatini" title="Rafael Sabatini">Rafael Sabatini</a> (1875–1950, Italy/England)</li>
<li><a href="/wiki/C._J._Sansom" title="C. J. Sansom">C. J. Sansom</a> (born 1952, Scotland)</li>
<li><a href="/wiki/Mitsugu_Saotome" title="Mitsugu Saotome">Mitsugu Saotome</a> (早乙女貢, 1926–2008, China/Japan)</li>
<li><a href="/wiki/Romain_Sardou" title="Romain Sardou">Romain Sardou</a> (born 1974, France)</li>
<li><a href="/wiki/Allen_Say" title="Allen Say">Allen Say</a> (born 1937, US)</li>
<li><a href="/wiki/Steven_Saylor" title="Steven Saylor">Steven Saylor</a> (born 1956, US)</li>
<li><a href="/wiki/Simon_Scarrow" title="Simon Scarrow">Simon Scarrow</a> (born 1962, England)</li>
<li><a href="/wiki/Nat_Schachner" title="Nat Schachner">Nat Schachner</a> (1895–1955, US)</li>
<li><a href="/wiki/Joseph_Viktor_von_Scheffel" class="mw-redirect" title="Joseph Viktor von Scheffel">Joseph Viktor von Scheffel</a> (1826–1886, Germany)</li>
<li><a href="/wiki/Bernhard_Schlink" title="Bernhard Schlink">Bernhard Schlink</a> (born 1944, Germany)</li>
<li><a href="/wiki/Lawrence_Schoonover" title="Lawrence Schoonover">Lawrence Schoonover</a> (1906–1980, US)</li>
<li><a href="/wiki/Rainer_M._Schr%C3%B6der" title="Rainer M. Schröder">Rainer M. Schröder</a> (born 1951, Germany)</li>
<li><a href="/wiki/Leonardo_Sciascia" title="Leonardo Sciascia">Leonardo Sciascia</a> (1921–1989, Italy)</li>
<li><a href="/wiki/Lawrence_Scott" title="Lawrence Scott">Lawrence Scott</a> (born 1943, Trinidad/England)</li>
<li><a href="/wiki/Susan_Holloway_Scott" title="Susan Holloway Scott">Susan Holloway Scott</a> (living, US)</li>
<li><a href="/wiki/Sir_Walter_Scott" class="mw-redirect" title="Sir Walter Scott">Sir Walter Scott</a> (1771–1832, Scotland)</li>
<li><a href="/wiki/Kate_Sedley" title="Kate Sedley">Kate Sedley</a> (born 1926, England)</li>
<li><a href="/wiki/Lisa_See" title="Lisa See">Lisa See</a> (born 1955, US)</li>
<li><a href="/wiki/Ram%C3%B3n_J._Sender" title="Ramón J. Sender">Ramón J. Sender</a> (1901–1982, Spain)</li>
<li><a href="/wiki/Ruta_Sepetys" title="Ruta Sepetys">Ruta Sepetys</a> (b. 1967, Lithuania/US)</li>
<li><a href="/wiki/Kate_Seredy" title="Kate Seredy">Kate Seredy</a> (1899–1975, US)</li>
<li><a href="/wiki/Anya_Seton" title="Anya Seton">Anya Seton</a> (1904–1990, US)</li>
<li><a href="/wiki/Tim_Severin" title="Tim Severin">Tim Severin</a> (1940–2020, England)</li>
<li><a href="/wiki/Jeffrey_Shaara" class="mw-redirect" title="Jeffrey Shaara">Jeffrey Shaara</a> (born 1952, US)</li>
<li><a href="/wiki/Michael_Shaara" title="Michael Shaara">Michael Shaara</a> (1928–1988, US)</li>
<li><a href="/wiki/Mary_Ann_Shaffer" title="Mary Ann Shaffer">Mary Ann Shaffer</a> (1934–2008, US)</li>
<li><a href="/wiki/Samuel_Shellabarger" title="Samuel Shellabarger">Samuel Shellabarger</a> (1888–1954, US)</li>
<li><a href="/wiki/Mary_Shelley" title="Mary Shelley">Mary Shelley</a> (1797–1851, England)</li>
<li><a href="/wiki/Joseph_Henry_Shorthouse" title="Joseph Henry Shorthouse">Joseph Henry Shorthouse</a> (1834–1903, England)</li>
<li><a href="/wiki/Henryk_Sienkiewicz" title="Henryk Sienkiewicz">Henryk Sienkiewicz</a> (1846–1916, Poland)</li>
<li><a href="/wiki/Germaine_Simon" title="Germaine Simon">Germaine Simon</a> (1921–2012, Luxembourg)</li>
<li><a href="/wiki/Ieva_Simonaityt%C4%97" title="Ieva Simonaitytė">Ieva Simonaitytė</a> (1897–1978, Lithuania)</li>
<li><a href="/wiki/Rebecca_Sinclair_(author)" title="Rebecca Sinclair (author)">Rebecca Sinclair</a> (living, US)</li>
<li><a href="/wiki/Sj%C3%B3n" title="Sjón">Sjón</a> (born 1962, Iceland)</li>
<li><a href="/wiki/Bertrice_Small" title="Bertrice Small">Bertrice Small</a> (1937–2015, US)</li>
<li><a href="/wiki/Wilbur_Smith" title="Wilbur Smith">Wilbur Smith</a> (born 1933, Northern Rhodesia/Zambia)</li>
<li><a href="/wiki/Alan_Spence" title="Alan Spence">Alan Spence</a> (born 1947, Scotland)</li>
<li><a href="/wiki/LaVyrle_Spencer" title="LaVyrle Spencer">LaVyrle Spencer</a> (1864–1926, England)</li>
<li><a href="/wiki/Armstrong_Sperry" title="Armstrong Sperry">Armstrong Sperry</a> (1897–1976, US)</li>
<li><a href="/wiki/Gy%C3%B6rgy_Spir%C3%B3" title="György Spiró">György Spiró</a> (born 1946, Hungary)</li>
<li><a href="/wiki/Francis_Spufford" title="Francis Spufford">Francis Spufford</a> (born 1964, England)</li>
<li><a href="/wiki/Eva_Stachniak" title="Eva Stachniak">Eva Stachniak</a> (born 1952, Poland/Canada)</li>
<li><a href="/wiki/David_Stacton" class="mw-redirect" title="David Stacton">David Stacton</a> (1923–1968, US)</li>
<li><a href="/wiki/Emiliyan_Stanev" title="Emiliyan Stanev">Emiliyan Stanev</a> (1907–1979, Bulgaria)</li>
<li><a href="/wiki/Louisa_Stanhope" title="Louisa Stanhope">Louisa Stanhope</a> (fl. 1806–1827, England)</li>
<li><a href="/wiki/Ludwik_Stasiak" title="Ludwik Stasiak">Ludwik Stasiak</a> (1858–1924, Poland)</li>
<li><a href="/wiki/Flora_Annie_Steel" title="Flora Annie Steel">Flora Annie Steel</a> (1847–1929, India/England)</li>
<li><a href="/wiki/Robert_Louis_Stevenson" title="Robert Louis Stevenson">Robert Louis Stevenson</a> (1850–1894, Scotland)</li>
<li><a href="/wiki/Mary_Stewart_(novelist)" title="Mary Stewart (novelist)">Mary Stewart</a> (1916–2014), England/Scotland)</li>
<li><a href="/wiki/Isabel_Stilwell" title="Isabel Stilwell">Isabel Stilwell</a> (b. 1960, Portugal)</li>
<li><a href="/wiki/Ilka_Stitz" title="Ilka Stitz">Ilka Stitz</a> (b. 1960, Germany)</li>
<li><a href="/wiki/Kathryn_Stockett" title="Kathryn Stockett">Kathryn Stockett</a> (born 1969, US)</li>
<li><a href="/wiki/Agnes_Strickland" title="Agnes Strickland">Agnes Strickland</a> (1796–1874, England)</li>
<li><a href="/wiki/Olga_Stringfellow" title="Olga Stringfellow">Olga Stringfellow</a> (b. 1921, New Zealand)</li>
<li><a href="/wiki/Ulrika_von_Strussenfelt" title="Ulrika von Strussenfelt">Ulrika von Strussenfelt</a> (1801–1873, Sweden)</li>
<li><a href="/wiki/Alex_Stuart_(writer)" class="mw-redirect" title="Alex Stuart (writer)">Alex Stuart</a>, <a href="/wiki/Robyn_Stuart" class="mw-redirect" title="Robyn Stuart">Robyn Stuart</a> and <a href="/wiki/Vivian_Stuart" title="Vivian Stuart">Vivian Stuart</a> (1914–1986, England)</li>
<li><a href="/wiki/Rosemary_Sutcliff" title="Rosemary Sutcliff">Rosemary Sutcliff</a> (1920–1992, England)</li>
<li><a href="/wiki/Magda_Szab%C3%B3" title="Magda Szabó">Magda Szabó</a> (1917–2007, Hungary)</li>
<li><a href="/wiki/No%C3%A9mi_Sz%C3%A9csi" title="Noémi Szécsi">Noémi Szécsi</a> (b. 1976, Hungary)</li>
<li><a href="/wiki/M%C3%A1ria_Szepes" title="Mária Szepes">Mária Szepes</a> (1908–2007, Hungary)</li></ul></div>
<h2><span class="mw-headline" id="T">T</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=List_of_historical_novelists&amp;action=edit&amp;section=20" title="Edit section: T">edit</a><span class="mw-editsection-bracket">]</span></span></h2>
<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r998391716"><div class="div-col" style="column-width: 20em;">
<ul><li><a href="/wiki/Karin_Tanabe" title="Karin Tanabe">Karin Tanabe</a> (living, US)</li>
<li><a href="/wiki/Reay_Tannahill" title="Reay Tannahill">Reay Tannahill</a> (1929–2007, Scotland/England)</li>
<li><a href="/wiki/Ellalice_Tate" class="mw-redirect" title="Ellalice Tate">Ellalice Tate</a> (1906–1993, England)</li>
<li><a href="/wiki/Janelle_Taylor" title="Janelle Taylor">Janelle Taylor</a> (born 1944, US)</li>
<li><a href="/wiki/William_Makepeace_Thackeray" title="William Makepeace Thackeray">William Makepeace Thackeray</a> (1811–1863, England)</li>
<li><a href="/wiki/James_Alexander_Thom" title="James Alexander Thom">James Alexander Thom</a> (born 1933, US)</li>
<li><a href="/wiki/Jodi_Thomas" title="Jodi Thomas">Jodi Thomas</a> (living, US)</li>
<li><a href="/wiki/Elizabeth_Thornton" title="Elizabeth Thornton">Elizabeth Thornton</a> (1940–2010,</li>
<li><a href="/wiki/Pramoedya_Ananta_Toer" title="Pramoedya Ananta Toer">Pramoedya Ananta Toer</a> (1925–2006, Dutch East Indies/Indonesia)</li>
<li><a href="/wiki/Colm_T%C3%B3ib%C3%ADn" title="Colm Tóibín">Colm Tóibín</a> (born 1955, Ireland)</li>
<li><a href="/wiki/Olga_Tokarczuk" title="Olga Tokarczuk">Olga Tokarczuk</a> (born 1962, Poland)</li>
<li><a href="/wiki/Aleksey_Konstantinovich_Tolstoy" title="Aleksey Konstantinovich Tolstoy">Aleksey Konstantinovich Tolstoy</a> (1817–1875, Russia)</li>
<li><a href="/wiki/Aleksey_Nikolayevich_Tolstoy" title="Aleksey Nikolayevich Tolstoy">Aleksey Nikolayevich Tolstoy</a> (1883–1945, Russia/Soviet Union)</li>
<li><a href="/wiki/Leo_Tolstoy" title="Leo Tolstoy">Leo Tolstoy</a> (1828–1910, Russia)</li>
<li><a href="/wiki/Theresa_Tomlinson" title="Theresa Tomlinson">Theresa Tomlinson</a> (born 1946, England)</li>
<li><a href="/wiki/Nigel_Tranter" title="Nigel Tranter">Nigel Tranter</a> (1909–2000, Scotland)</li>
<li><a href="/wiki/Geoffrey_Trease" title="Geoffrey Trease">Geoffrey Trease</a> (1909–1998, England)</li>
<li><a href="/wiki/Henry_Treece" title="Henry Treece">Henry Treece</a> (1911–1966, England)</li>
<li><a href="/wiki/Rose_Tremain" title="Rose Tremain">Rose Tremain</a> (born 1943, England)</li>
<li><a href="/wiki/Peter_Berresford_Ellis" title="Peter Berresford Ellis">Peter Tremayne</a> (born 1943, England)</li>
<li><a href="/wiki/Meriol_Trevor" title="Meriol Trevor">Meriol Trevor</a> (1919–2000, England)</li>
<li><a href="/wiki/Joanna_Trollope" title="Joanna Trollope">Joanna Trollope</a> ((born 1943, England)</li>
<li><a href="/wiki/Anthony_Trollope" title="Anthony Trollope">Anthony Trollope</a> (1815–1882, England)</li>
<li><a href="/wiki/Stefan_Tsanev" title="Stefan Tsanev">Stefan Tsanev</a> (born 1936, Bulgaria)</li>
<li><a href="/wiki/Kunio_Tsuji" title="Kunio Tsuji">Kunio Tsuji</a> (1925–1999,</li>
<li><a href="/wiki/Elizabeth_Tudor" class="mw-redirect" title="Elizabeth Tudor">Elizabeth Tudor</a> (Lady Hasanova, b. 1978, Azerbaijan)</li>
<li><a href="/wiki/Ann_Turnbull" title="Ann Turnbull">Ann Turnbull</a> (born 1943, England)</li>
<li><a href="/wiki/Harry_Turtledove" title="Harry Turtledove">Harry Turtledove</a> (born 1949, US)</li></ul></div>
<h2><span class="mw-headline" id="U">U</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=List_of_historical_novelists&amp;action=edit&amp;section=21" title="Edit section: U">edit</a><span class="mw-editsection-bracket">]</span></span></h2>
<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r998391716"><div class="div-col" style="column-width: 20em;">
<ul><li><a href="/wiki/Max_Uhlemann" title="Max Uhlemann">Max Uhlemann</a> (died 1862, Germany)</li>
<li><a href="/wiki/Barry_Unsworth" title="Barry Unsworth">Barry Unsworth</a> (1930–2012, England/Italy)</li>
<li><a href="/wiki/Leon_Uris" title="Leon Uris">Leon Uris</a> (1924–2003, US)</li>
<li><a href="/wiki/Anne_Ursu" title="Anne Ursu">Anne Ursu</a> (living, US)</li></ul></div>
<h2><span class="mw-headline" id="V">V</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=List_of_historical_novelists&amp;action=edit&amp;section=22" title="Edit section: V">edit</a><span class="mw-editsection-bracket">]</span></span></h2>
<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r998391716"><div class="div-col" style="column-width: 20em;">
<ul><li><a href="/wiki/Andrew_Vachss" title="Andrew Vachss">Andrew Vachss</a> (born 1942, US)</li>
<li><a href="/wiki/Robert_Van_Gulik" class="mw-redirect" title="Robert Van Gulik">Robert Van Gulik</a> (1910–1967, Netherlands/Indonesia)</li>
<li><a href="/wiki/Guy_Vanderhaeghe" title="Guy Vanderhaeghe">Guy Vanderhaeghe</a> (born 1951, Canada)</li>
<li><a href="/wiki/Carl_Franz_van_der_Velde" title="Carl Franz van der Velde">Carl Franz van der Velde</a> (1779–1824, Germany)</li>
<li><a href="/wiki/Caroline_Vermalle" title="Caroline Vermalle">Caroline Vermalle</a> (born 1973, France)</li>
<li><a href="/wiki/Elena_Maria_Vidal" title="Elena Maria Vidal">Elena Maria Vidal</a> (born 1962, US)</li>
<li><a href="/wiki/Gore_Vidal" title="Gore Vidal">Gore Vidal</a> (1925–2012, US)</li>
<li><a href="/wiki/Rene_Villanueva" title="Rene Villanueva">Rene Villanueva</a> (1954–2007, Philippines)</li>
<li><a href="/wiki/Elfrida_Vipont" title="Elfrida Vipont">Elfrida Vipont</a> (1902–1992, England)</li>
<li><a href="/wiki/Simone_van_der_Vlugt" title="Simone van der Vlugt">Simone van der Vlugt</a> (b. 1966, Netherlands)</li>
<li><a href="/wiki/William_T._Vollmann" title="William T. Vollmann">William T. Vollmann</a> (1959, US)</li>
<li><a href="/wiki/Anne_de_Vries" title="Anne de Vries">Anne de Vries</a> (1904–1964, Netherlands)</li></ul></div>
<h2><span class="mw-headline" id="W">W</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=List_of_historical_novelists&amp;action=edit&amp;section=23" title="Edit section: W">edit</a><span class="mw-editsection-bracket">]</span></span></h2>
<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r998391716"><div class="div-col" style="column-width: 20em;">
<ul><li><a href="/wiki/Lea_Wait" title="Lea Wait">Lea Wait</a> (born 1946, US)</li>
<li><a href="/wiki/Lew_Wallace" title="Lew Wallace">Lew Wallace</a> (1827–1905, US)</li>
<li><a href="/wiki/Jill_Paton_Walsh" title="Jill Paton Walsh">Jill Paton Walsh</a> (born 1937, England)</li>
<li><a href="/wiki/Mika_Waltari" title="Mika Waltari">Mika Waltari</a> (1908–1979, Finland)</li>
<li><a href="/wiki/Sarah_Waters" title="Sarah Waters">Sarah Waters</a> (born 1966, Wales)</li>
<li><a href="/wiki/Evelyn_Waugh" title="Evelyn Waugh">Evelyn Waugh</a> (1903–1966, England)</li>
<li><a href="/wiki/Catherine_Webb" title="Catherine Webb">Catherine Webb</a> (born 1986, England)</li>
<li><a href="/wiki/Alison_Weir" title="Alison Weir">Alison Weir</a> (born 1951, England)</li>
<li><a href="/wiki/Ronald_Welch" title="Ronald Welch">Ronald Welch</a> (1909–1982, Wales/England)</li>
<li><a href="/wiki/Percy_F._Westerman" title="Percy F. Westerman">Percy F. Westerman</a> (1876–1959, England)</li>
<li><a href="/wiki/Helena_Westermarck" title="Helena Westermarck">Helena Westermarck</a> (1857–1938), Finland)</li>
<li><a href="/wiki/Stanley_J._Weyman" title="Stanley J. Weyman">Stanley J. Weyman</a> (1855–1928, England)</li>
<li><a href="/wiki/Richard_S._Wheeler" title="Richard S. Wheeler">Richard S. Wheeler</a> (born 1935, US)</li>
<li><a href="/wiki/Charles_Whistler" title="Charles Whistler">Charles Whistler</a> (1856–1913, England)</li>
<li><a href="/wiki/T._H._White" title="T. H. White">T. H. White</a> (1906–1964, England)</li>
<li><a href="/wiki/George_Whyte-Melville" title="George Whyte-Melville">George Whyte-Melville</a> (1821–1878, Scotland)</li>
<li><a href="/wiki/Anne_Wignall" title="Anne Wignall">Anne Wignall</a> (1912–1982, England)</li>
<li><a href="/wiki/Thornton_Wilder" title="Thornton Wilder">Thornton Wilder</a> (1897–1975, US)</li>
<li><a href="/wiki/Jay_Williams_(author)" title="Jay Williams (author)">Jay Williams</a> (1914–1978, US)</li>
<li><a href="/wiki/Maiya_Williams" title="Maiya Williams">Maiya Williams</a> (born 1962, US)</li>
<li><a href="/wiki/Carole_Wilkinson" title="Carole Wilkinson">Carole Wilkinson</a> (born 1950, Australia)</li>
<li><a href="/wiki/Jacqueline_Winspear" title="Jacqueline Winspear">Jacqueline Winspear</a> (born 1955, England)</li>
<li><a href="/wiki/Barbara_Wood" title="Barbara Wood">Barbara Wood</a> (born 1947, US)</li>
<li><a href="/wiki/Richard_Woodman" title="Richard Woodman">Richard Woodman</a> (born 1944, England)</li>
<li><a href="/wiki/Herman_Wouk" title="Herman Wouk">Herman Wouk</a> (1915–2019, US)</li></ul></div>
<h2><span class="mw-headline" id="Y">Y</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=List_of_historical_novelists&amp;action=edit&amp;section=24" title="Edit section: Y">edit</a><span class="mw-editsection-bracket">]</span></span></h2>
<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r998391716"><div class="div-col" style="column-width: 20em;">
<ul><li><a href="/wiki/Yamada_Bimy%C5%8D" title="Yamada Bimyō">Yamada Bimyō</a> (山田 美妙, 1868–1910, Japan)</li>
<li><a href="/wiki/Sh%C5%ABgor%C5%8D_Yamamoto" title="Shūgorō Yamamoto">Shūgorō Yamamoto</a> (山本周五郎, 1903–1967, Japan)</li>
<li><a href="/wiki/Chelsea_Quinn_Yarbro" title="Chelsea Quinn Yarbro">Chelsea Quinn Yarbro</a> (born 1942, US)</li>
<li><a href="/wiki/Yana_Yazova" title="Yana Yazova">Yana Yazova</a> (1912–1974, Bulgaria)</li>
<li><a href="/wiki/Frank_Yerby" title="Frank Yerby">Frank Yerby</a> (1916–1991, US)</li>
<li><a href="/wiki/Simon_Hawke" title="Simon Hawke">Nicholas Yermakov</a> (born 1951, US)</li>
<li><a href="/wiki/Jane_Yolen" title="Jane Yolen">Jane Yolen</a> (born 1939, US)</li>
<li><a href="/wiki/Charlotte_Mary_Yonge" title="Charlotte Mary Yonge">Charlotte Mary Yonge</a> (1823–1901, England)</li>
<li><a href="/wiki/Eiji_Yoshikawa" title="Eiji Yoshikawa">Eiji Yoshikawa</a> (吉川 英治, 1892–1962, Japan)</li></ul></div>
<h2><span class="mw-headline" id="Z">Z</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=List_of_historical_novelists&amp;action=edit&amp;section=25" title="Edit section: Z">edit</a><span class="mw-editsection-bracket">]</span></span></h2>
<link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r998391716"><div class="div-col" style="column-width: 20em;">
<ul><li><a href="/wiki/Stoyan_Zagorchinov" title="Stoyan Zagorchinov">Stoyan Zagorchinov</a> (1889–1969, Bulgaria)</li>
<li><a href="/wiki/Mikhail_Zagoskin" title="Mikhail Zagoskin">Mikhail Zagoskin</a> (1789–1852, Russia)</li>
<li><a href="/wiki/Lajos_Zilahy" title="Lajos Zilahy">Lajos Zilahy</a> (1891–1974, Hungary)</li>
<li><a href="/wiki/Richard_Zimler" title="Richard Zimler">Richard Zimler</a> (born 1956, US)</li>
<li><a href="/wiki/Karl_Zuchardt" title="Karl Zuchardt">Karl Zuchardt</a> (1887–1968, Germany)</li>
<li><a href="/wiki/Markus_Zusak" title="Markus Zusak">Markus Zusak</a> (born 1975, Australia)</li></ul></div>
<h2><span class="mw-headline" id="See_also">See also</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=List_of_historical_novelists&amp;action=edit&amp;section=26" title="Edit section: See also">edit</a><span class="mw-editsection-bracket">]</span></span></h2>
<ul><li><a href="/wiki/List_of_writers" class="mw-redirect" title="List of writers">List of writers</a></li></ul>
<!-- 
NewPP limit report
Parsed by mw1289
Cached time: 20210424133249
Cache expiry: 2592000
Dynamic content: false
Complications: []
CPU time usage: 0.424 seconds
Real time usage: 0.529 seconds
Preprocessor visited node count: 2912/1000000
Post‐expand include size: 146765/2097152 bytes
Template argument size: 132723/2097152 bytes
Highest expansion depth: 19/40
Expensive parser function count: 1/500
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 12161/5000000 bytes
Lua time usage: 0.060/10.000 seconds
Lua memory usage: 2157738/52428800 bytes
Number of Wikibase entities loaded: 0/400
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%  282.277      1 -total
 49.98%  141.078     24 Template:Columns-list
 40.81%  115.201      1 Template:Expand_list
 33.06%   93.328     24 Template:Div_col
 26.98%   76.169      1 Template:Hatnote
 21.75%   61.386     25 Template:Main_other
 15.30%   43.202      1 Template:TDMCA
 13.29%   37.520      1 Template:DMCA
 11.33%   31.971      1 Template:Dated_maintenance_category
  7.77%   21.933      1 Template:TOC_right
-->

<!-- Saved in parser cache with key enwiki:pcache:idhash:85422-0!canonical and timestamp 20210424133250 and revision id 1019630439. Serialized with JSON.
 -->
</div>
"""

soup = BeautifulSoup(authors, 'html.parser')
with open('authors2.txt', 'w', encoding='utf-8') as f:
    for data in soup.find_all('div', attrs={'class': 'div-col'}):
        for d in data.find_all('li'):
            f.write(d.find('a').get_text())
            f.write("\n")