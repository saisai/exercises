from bs4 import BeautifulSoup

author = """
<tbody>
<tr>
<td><span class="nowrap"><span data-sort-value="Shakespeare, William"><span class="vcard"><span class="fn"><a href="/wiki/William_Shakespeare" title="William Shakespeare">William Shakespeare</a></span></span></span></span>
</td>
<td data-sort-value="2,000 million">2 billion<sup id="cite_ref-1" class="reference"><a href="#cite_note-1">[1]</a></sup>
</td>
<td data-sort-value="4,000 million">4 billion<sup id="cite_ref-Shakespeare_2-0" class="reference"><a href="#cite_note-Shakespeare-2">[2]</a></sup>
</td>
<td><a href="/wiki/English_language" title="English language">English</a>
</td>
<td><a href="/wiki/Shakespeare%27s_plays" title="Shakespeare's plays">Plays</a> and <a href="/wiki/Shakespeare%27s_sonnets" title="Shakespeare's sonnets">poetry</a>
</td>
<td>42
</td>
<td><a href="/wiki/Kingdom_of_England" title="Kingdom of England">English</a>
</td></tr>
<tr>
<td><span data-sort-value="Christie, Agatha"><span class="vcard"><span class="fn"><a href="/wiki/Agatha_Christie" title="Agatha Christie">Agatha Christie</a></span></span></span>
</td>
<td data-sort-value="2,000 million">2 billion<sup id="cite_ref-3" class="reference"><a href="#cite_note-3">[3]</a></sup>
</td>
<td data-sort-value="4,000 million">4 billion<sup id="cite_ref-Shakespeare_2-1" class="reference"><a href="#cite_note-Shakespeare-2">[2]</a></sup>
</td>
<td>English
</td>
<td><a href="/wiki/Whodunit" title="Whodunit">Whodunits</a> including the <i><a href="/wiki/Miss_Marple" title="Miss Marple">Miss Marple</a></i> and <i><a href="/wiki/Hercule_Poirot" title="Hercule Poirot">Hercule Poirot</a></i> series
</td>
<td>85
</td>
<td><a href="/wiki/Kingdom_of_England" title="Kingdom of England">English</a>
</td></tr>
<tr>
<td><span data-sort-value="Cartland, Barbara"><span class="vcard"><span class="fn"><a href="/wiki/Barbara_Cartland" title="Barbara Cartland">Barbara Cartland</a></span></span></span>
</td>
<td>500 million<sup id="cite_ref-4" class="reference"><a href="#cite_note-4">[4]</a></sup>
</td>
<td data-sort-value="1,000 million">1 billion<sup id="cite_ref-5" class="reference"><a href="#cite_note-5">[5]</a></sup>
</td>
<td>English
</td>
<td><a href="/wiki/Romance_novel" title="Romance novel">Romance</a>
</td>
<td>723
</td>
<td><a href="/wiki/Kingdom_of_England" title="Kingdom of England">English</a>
</td></tr>
<tr>
<td><span data-sort-value="Steel, Danielle"><span class="vcard"><span class="fn"><a href="/wiki/Danielle_Steel" title="Danielle Steel">Danielle Steel</a></span></span></span>
</td>
<td>500 million<sup id="cite_ref-6" class="reference"><a href="#cite_note-6">[6]</a></sup>
</td>
<td>800 million<sup id="cite_ref-7" class="reference"><a href="#cite_note-7">[7]</a></sup>
</td>
<td>English
</td>
<td>General fiction, Romance
</td>
<td>179
</td>
<td><a href="/wiki/United_States" title="United States">American</a>
</td></tr>
<tr>
<td><span data-sort-value="Robbins, Harold"><span class="vcard"><span class="fn"><a href="/wiki/Harold_Robbins" title="Harold Robbins">Harold Robbins</a></span></span></span>
</td>
<td>750 million<sup id="cite_ref-8" class="reference"><a href="#cite_note-8">[8]</a></sup>
</td>
<td>750 million<sup id="cite_ref-9" class="reference"><a href="#cite_note-9">[9]</a></sup>
</td>
<td>English
</td>
<td><a href="/wiki/Adventure_novel" class="mw-redirect" title="Adventure novel">Adventure</a>
</td>
<td>23
</td>
<td><a href="/wiki/United_States" title="United States">American</a>
</td></tr>
<tr>
<td><span data-sort-value="Simenon, Georges"><span class="vcard"><span class="fn"><a href="/wiki/Georges_Simenon" title="Georges Simenon">Georges Simenon</a></span></span></span>
</td>
<td>500 million<sup id="cite_ref-10" class="reference"><a href="#cite_note-10">[10]</a></sup>
</td>
<td>700 million<sup id="cite_ref-11" class="reference"><a href="#cite_note-11">[11]</a></sup>
</td>
<td><a href="/wiki/French_language" title="French language">French</a>
</td>
<td>Detectives, <i><a href="/wiki/Maigret" class="mw-redirect" title="Maigret">Maigret</a></i>, romans dur
</td>
<td>570
</td>
<td><a href="/wiki/Belgium" title="Belgium">Belgian</a>
</td></tr>
<tr>
<td><span data-sort-value="Blyton, Enid"><span class="vcard"><span class="fn"><a href="/wiki/Enid_Blyton" title="Enid Blyton">Enid Blyton</a></span></span></span>
</td>
<td>
</td>
<td>600 million<sup id="cite_ref-12" class="reference"><a href="#cite_note-12">[12]</a></sup>
</td>
<td>English
</td>
<td><a href="/wiki/Children%27s_literature" title="Children's literature">Children's literature</a>, <i><a href="/wiki/Noddy_(character)" title="Noddy (character)">Noddy</a></i>, <i><a href="/wiki/The_Famous_Five_(novel_series)" title="The Famous Five (novel series)">The Famous Five</a></i>, <i><a href="/wiki/The_Secret_Seven" title="The Secret Seven">The Secret Seven</a></i>
</td>
<td>800
</td>
<td><a href="/wiki/Kingdom_of_England" title="Kingdom of England">English</a>
</td></tr>
<tr>
<td><span data-sort-value="Sheldon, Sidney"><span class="vcard"><span class="fn"><a href="/wiki/Sidney_Sheldon" title="Sidney Sheldon">Sidney Sheldon</a></span></span></span>
</td>
<td>370 million<sup id="cite_ref-13" class="reference"><a href="#cite_note-13">[13]</a></sup>
</td>
<td>600 million<sup id="cite_ref-14" class="reference"><a href="#cite_note-14">[14]</a></sup>
</td>
<td>English
</td>
<td><a href="/wiki/Suspense_fiction" class="mw-redirect" title="Suspense fiction">Suspense</a>
</td>
<td>21
</td>
<td><a href="/wiki/United_States" title="United States">American</a>
</td></tr>
<tr>
<td><span data-sort-value="Rowling, J. K."><span class="vcard"><span class="fn"><a href="/wiki/J._K._Rowling" title="J. K. Rowling">J. K. Rowling</a></span></span></span>
</td>
<td>500 million<sup id="cite_ref-pottermore_15-0" class="reference"><a href="#cite_note-pottermore-15">[15]</a></sup>
</td>
<td>500 million<sup id="cite_ref-pottermore_15-1" class="reference"><a href="#cite_note-pottermore-15">[15]</a></sup>
</td>
<td>English
</td>
<td><i><a href="/wiki/Harry_Potter" title="Harry Potter">Harry Potter</a></i>, <i><a href="/wiki/Fantastic_Beasts_and_Where_to_Find_Them" title="Fantastic Beasts and Where to Find Them">Fantastic Beasts and Where to Find Them</a></i>, <i><a href="/wiki/Cormoran_Strike" title="Cormoran Strike">Cormoran Strike</a></i>, <a href="/wiki/Fantasy_novel" class="mw-redirect" title="Fantasy novel">fantasy</a>, <a href="/wiki/Crime_fiction" title="Crime fiction">crime fiction</a>
</td>
<td>15
</td>
<td><a href="/wiki/British_people" title="British people">British</a>
</td></tr>
<tr>
<td><span data-sort-value="Patten, Gilbert"><span class="vcard"><span class="fn"><a href="/wiki/Gilbert_Patten" title="Gilbert Patten">Gilbert Patten</a></span></span></span>
</td>
<td>125 million<sup id="cite_ref-16" class="reference"><a href="#cite_note-16">[16]</a></sup>
</td>
<td>500 million<sup id="cite_ref-17" class="reference"><a href="#cite_note-17">[17]</a></sup>
</td>
<td>English
</td>
<td>Adolescent adventures
</td>
<td>209
</td>
<td><a href="/wiki/United_States" title="United States">American</a>
</td></tr>
<tr>
<td><span data-sort-value="Seuss, Dr."><span class="vcard"><span class="fn"><a href="/wiki/Dr._Seuss" title="Dr. Seuss">Dr. Seuss</a></span></span></span>
</td>
<td>100 million<sup id="cite_ref-18" class="reference"><a href="#cite_note-18">[18]</a></sup>
</td>
<td>500 million<sup id="cite_ref-19" class="reference"><a href="#cite_note-19">[19]</a></sup>
</td>
<td>English
</td>
<td>Children's literature
</td>
<td>44
</td>
<td><a href="/wiki/United_States" title="United States">American</a>
</td></tr>
<tr>
<td><span data-sort-value="Oda, Eiichiro"><span class="vcard"><span class="fn"><a href="/wiki/Eiichiro_Oda" title="Eiichiro Oda">Eiichiro Oda</a></span></span></span>
</td>
<td>
</td>
<td>480&nbsp;million<sup id="cite_ref-20" class="reference"><a href="#cite_note-20">[20]</a></sup><sup id="cite_ref-21" class="reference"><a href="#cite_note-21">[21]</a></sup>
</td>
<td><a href="/wiki/Japanese_language" title="Japanese language">Japanese</a>
</td>
<td><a href="/wiki/Manga" title="Manga">Manga</a>, <i><a href="/wiki/One_Piece" title="One Piece">One Piece</a></i>
</td>
<td>98
</td>
<td><a href="/wiki/Japan" title="Japan">Japanese</a>
</td></tr>
<tr>
<td><span data-sort-value="Tolstoy, Leo"><span class="vcard"><span class="fn"><a href="/wiki/Leo_Tolstoy" title="Leo Tolstoy">Leo Tolstoy</a></span></span></span>
</td>
<td>
</td>
<td>413 million<sup id="cite_ref-NYTIMES1987_22-0" class="reference"><a href="#cite_note-NYTIMES1987-22">[22]</a></sup>
</td>
<td><a href="/wiki/Russian_language" title="Russian language">Russian</a>
</td>
<td><i><a href="/wiki/War_and_Peace" title="War and Peace">War and Peace</a></i>, <i><a href="/wiki/Anna_Karenina" title="Anna Karenina">Anna Karenina</a></i>
</td>
<td>48
</td>
<td><a href="/wiki/Russia" title="Russia">Russian</a>
</td></tr>
<tr>
<td><span data-sort-value="Tellado, Corín"><span class="vcard"><span class="fn"><a href="/wiki/Cor%C3%ADn_Tellado" title="Corín Tellado">Corín Tellado</a></span></span></span>
</td>
<td>400 million<sup id="cite_ref-23" class="reference"><a href="#cite_note-23">[23]</a></sup>
</td>
<td>400 million<sup id="cite_ref-24" class="reference"><a href="#cite_note-24">[24]</a></sup>
</td>
<td><a href="/wiki/Spanish_language" title="Spanish language">Spanish</a>
</td>
<td><a href="/wiki/Romance_novel" title="Romance novel">Romance</a>
</td>
<td>4,000
</td>
<td><a href="/wiki/Spain" title="Spain">Spanish</a>
</td></tr>
<tr>
<td><span data-sort-value="Collins, Jackie"><span class="vcard"><span class="fn"><a href="/wiki/Jackie_Collins" title="Jackie Collins">Jackie Collins</a></span></span></span>
</td>
<td>250 million<sup id="cite_ref-25" class="reference"><a href="#cite_note-25">[25]</a></sup>
</td>
<td>400 million<sup id="cite_ref-26" class="reference"><a href="#cite_note-26">[26]</a></sup>
</td>
<td>English
</td>
<td><a href="/wiki/Romance_novel" title="Romance novel">Romance</a>
</td>
<td>25
</td>
<td><a href="/wiki/Kingdom_of_England" title="Kingdom of England">English</a>
</td></tr>
<tr>
<td><span data-sort-value="Alger, Horatio"><span class="vcard"><span class="fn"><a href="/wiki/Horatio_Alger" title="Horatio Alger">Horatio Alger</a></span></span></span>
</td>
<td>200 million<sup id="cite_ref-27" class="reference"><a href="#cite_note-27">[27]</a></sup>
</td>
<td>400 million<sup id="cite_ref-28" class="reference"><a href="#cite_note-28">[28]</a></sup>
</td>
<td>English
</td>
<td><a href="/wiki/Dime_novel" title="Dime novel">Dime novels</a>
</td>
<td>135
</td>
<td>American
</td></tr>
<tr>
<td><span data-sort-value="Stine, R. L."><span class="vcard"><span class="fn"><a href="/wiki/R._L._Stine" title="R. L. Stine">R. L. Stine</a></span></span></span>
</td>
<td>100 million<sup id="cite_ref-29" class="reference"><a href="#cite_note-29">[29]</a></sup>
</td>
<td>400 million<sup id="cite_ref-30" class="reference"><a href="#cite_note-30">[30]</a></sup>
</td>
<td>English
</td>
<td><i><a href="/wiki/Goosebumps" title="Goosebumps">Goosebumps</a></i> series, <i><a href="/wiki/Fear_Street" title="Fear Street">Fear Street</a></i> series, horror, comedy
</td>
<td>430+
</td>
<td>American
</td></tr>
<tr>
<td><span data-sort-value="Koontz, Dean"><span class="vcard"><span class="fn"><a href="/wiki/Dean_Koontz" title="Dean Koontz">Dean Koontz</a></span></span></span>
</td>
<td>325 million<sup id="cite_ref-31" class="reference"><a href="#cite_note-31">[31]</a></sup>
</td>
<td>400 million<sup id="cite_ref-32" class="reference"><a href="#cite_note-32">[32]</a></sup>
</td>
<td>English
</td>
<td><a href="/wiki/Horror_fiction" title="Horror fiction">Horror</a>, <a href="/wiki/Thriller_fiction" class="mw-redirect" title="Thriller fiction">thriller</a>, <a href="/wiki/Science_fiction" title="Science fiction">science fiction</a>, <a href="/wiki/Fantasy_novel" class="mw-redirect" title="Fantasy novel">fantasy</a>
</td>
<td>91
</td>
<td>American
</td></tr>
<tr>
<td><span data-sort-value="Roberts, Nora"><span class="vcard"><span class="fn"><a href="/wiki/Nora_Roberts" title="Nora Roberts">Nora Roberts</a></span></span></span>
</td>
<td>145 million<sup id="cite_ref-33" class="reference"><a href="#cite_note-33">[33]</a></sup>
</td>
<td>400 million<sup id="cite_ref-34" class="reference"><a href="#cite_note-34">[34]</a></sup>
</td>
<td>English
</td>
<td>Romance
</td>
<td>200+
</td>
<td>American
</td></tr>
<tr>
<td><span data-sort-value="Pushkin, Alexander"><span class="vcard"><span class="fn"><a href="/wiki/Alexander_Pushkin" title="Alexander Pushkin">Alexander Pushkin</a></span></span></span>
</td>
<td>
</td>
<td>357 million<sup id="cite_ref-NYTIMES1987_22-1" class="reference"><a href="#cite_note-NYTIMES1987-22">[22]</a></sup>
</td>
<td>Russian
</td>
<td>Plays, poetry, prose, <i><a href="/wiki/Eugene_Onegin" title="Eugene Onegin">Eugene Onegin</a></i>
</td>
<td>17
</td>
<td>Russian
</td></tr>
<tr>
<td><span data-sort-value="King, Stephen"><span class="vcard"><span class="fn"><a href="/wiki/Stephen_King" title="Stephen King">Stephen King</a></span></span></span>
</td>
<td>300 million<sup id="cite_ref-35" class="reference"><a href="#cite_note-35">[35]</a></sup>
</td>
<td>350 million<sup id="cite_ref-36" class="reference"><a href="#cite_note-36">[36]</a></sup>
</td>
<td>English
</td>
<td><a href="/wiki/Horror_fiction" title="Horror fiction">Horror</a>, <a href="/wiki/Science_fiction" title="Science fiction">science fiction</a>, <a href="/wiki/Fantasy_literature" title="Fantasy literature">fantasy</a>, <i><a href="/wiki/It_(novel)" title="It (novel)">It</a></i>, <i><a href="/wiki/The_Shining_(novel)" title="The Shining (novel)">The Shining</a></i>, <i><a href="/wiki/The_Stand" title="The Stand">The Stand</a></i>, <i><a href="/wiki/Pet_Sematary" title="Pet Sematary">Pet Sematary</a></i>, <i><a href="/wiki/Salem%27s_Lot" class="mw-redirect" title="Salem's Lot">Salem's Lot</a></i>, <i><a href="/wiki/The_Green_Mile_(novel)" title="The Green Mile (novel)">The Green Mile</a></i>
</td>
<td>77
</td>
<td>American
</td></tr>
<tr>
<td><span data-sort-value="Coelho, Paulo"><span class="vcard"><span class="fn"><a href="/wiki/Paulo_Coelho" title="Paulo Coelho">Paulo Coelho</a></span></span></span>
</td>
<td>225 million<sup id="cite_ref-37" class="reference"><a href="#cite_note-37">[37]</a></sup>
</td>
<td>350 million<sup id="cite_ref-38" class="reference"><a href="#cite_note-38">[38]</a></sup>
</td>
<td><a href="/wiki/Portuguese_language" title="Portuguese language">Portuguese</a>
</td>
<td><i><a href="/wiki/The_Alchemist_(novel)" title="The Alchemist (novel)">The Alchemist</a></i>
</td>
<td>28
</td>
<td><a href="/wiki/Brazil" title="Brazil">Brazilian</a>
</td></tr>
<tr>
<td><span data-sort-value="Archer, Jeffrey"><span class="vcard"><span class="fn"><a href="/wiki/Jeffrey_Archer" title="Jeffrey Archer">Jeffrey Archer</a></span></span></span>
</td>
<td>250 million<sup id="cite_ref-39" class="reference"><a href="#cite_note-39">[39]</a></sup>
</td>
<td>330 million<sup id="cite_ref-40" class="reference"><a href="#cite_note-40">[40]</a></sup>
</td>
<td>English
</td>
<td><a href="/wiki/Saga" title="Saga">Saga</a>, <a href="/wiki/Thriller_fiction" class="mw-redirect" title="Thriller fiction">thriller</a>, <a href="/wiki/Short_stories" class="mw-redirect" title="Short stories">short stories</a>, <i><a href="/wiki/Kane_and_Abel_(novel)" title="Kane and Abel (novel)"><i>Kane and Abel</i></a></i>, <i><a href="/wiki/The_Clifton_Chronicles" class="mw-redirect" title="The Clifton Chronicles">The Clifton Chronicles</a></i>
</td>
<td>33
</td>
<td><a href="/wiki/Kingdom_of_England" title="Kingdom of England">English</a>
</td></tr>
<tr>
<td><span data-sort-value="L'Amour, Louis"><span class="vcard"><span class="fn"><a href="/wiki/Louis_L%27Amour" title="Louis L'Amour">Louis L'Amour</a></span></span></span>
</td>
<td>230 million<sup id="cite_ref-41" class="reference"><a href="#cite_note-41">[41]</a></sup>
</td>
<td>330 million<sup id="cite_ref-42" class="reference"><a href="#cite_note-42">[42]</a></sup>
</td>
<td>English
</td>
<td><a href="/wiki/Western_fiction" title="Western fiction">Western</a>
</td>
<td>101
</td>
<td>American
</td></tr>
<tr>
<td><span data-sort-value="Akagawa, Jirō"><span class="vcard"><span class="fn"><a href="/wiki/Jir%C5%8D_Akagawa" title="Jirō Akagawa">Jirō Akagawa</a></span></span></span>
</td>
<td>300 million<sup id="cite_ref-43" class="reference"><a href="#cite_note-43">[43]</a></sup>
</td>
<td>330 million<sup id="cite_ref-44" class="reference"><a href="#cite_note-44">[44]</a></sup>
</td>
<td>Japanese
</td>
<td>Mystery
</td>
<td>500+
</td>
<td><a href="/wiki/Japanese_people" title="Japanese people">Japanese</a>
</td></tr>
<tr>
<td><span data-sort-value="Goscinny, René"><span class="vcard"><span class="fn"><a href="/wiki/Ren%C3%A9_Goscinny" title="René Goscinny">René Goscinny</a></span></span></span>
</td>
<td>
</td>
<td>325<span class="nowrap">&nbsp;</span>million<sup id="cite_ref-Volumes-sold_45-0" class="reference"><a href="#cite_note-Volumes-sold-45">[45]</a></sup>
</td>
<td>French
</td>
<td><a href="/wiki/Franco-Belgian_comics" class="mw-redirect" title="Franco-Belgian comics">Franco-Belgian comics</a>, <i><a href="/wiki/Asterix" title="Asterix">Asterix</a></i>, <i><a href="/wiki/Lucky_Luke" title="Lucky Luke">Lucky Luke</a></i>, <i><a href="/wiki/Iznogoud" title="Iznogoud">Iznogoud</a></i>
</td>
<td>108
</td>
<td><a href="/wiki/France" title="France">French</a>
</td></tr>
<tr>
<td><span data-sort-value="Gardner, Erle Stanley"><span class="vcard"><span class="fn"><a href="/wiki/Erle_Stanley_Gardner" title="Erle Stanley Gardner">Erle Stanley Gardner</a></span></span></span>
</td>
<td>100 million<sup id="cite_ref-46" class="reference"><a href="#cite_note-46">[46]</a></sup>
</td>
<td>325 million<sup id="cite_ref-47" class="reference"><a href="#cite_note-47">[47]</a></sup>
</td>
<td>English
</td>
<td><a href="/wiki/Mystery_(fiction)" class="mw-redirect" title="Mystery (fiction)">Mystery</a>, <i><a href="/wiki/Perry_Mason" title="Perry Mason">Perry Mason</a></i>
</td>
<td>140
</td>
<td>American
</td></tr>
<tr>
<td><span data-sort-value="Wallace, Edgar"><span class="vcard"><span class="fn"><a href="/wiki/Edgar_Wallace" title="Edgar Wallace">Edgar Wallace</a></span></span></span>
</td>
<td>
</td>
<td>300 million<sup id="cite_ref-48" class="reference"><a href="#cite_note-48">[48]</a></sup>
</td>
<td>English
</td>
<td>Detective
</td>
<td>175
</td>
<td><a href="/wiki/Kingdom_of_England" title="Kingdom of England">English</a>
</td></tr>
<tr>
<td><a href="/wiki/Jin_Yong" title="Jin Yong">Jin Yong</a>
</td>
<td>100 million<sup id="cite_ref-49" class="reference"><a href="#cite_note-49">[49]</a></sup>
</td>
<td>300 million<sup id="cite_ref-50" class="reference"><a href="#cite_note-50">[50]</a></sup><sup id="cite_ref-51" class="reference"><a href="#cite_note-51">[51]</a></sup>
</td>
<td><a href="/wiki/Chinese_language" title="Chinese language">Chinese</a>
</td>
<td><a href="/wiki/Wuxia" title="Wuxia">Wuxia</a>
</td>
<td>15
</td>
<td><a href="/wiki/China" title="China">Chinese</a>
</td></tr>
<tr>
<td><span data-sort-value="Dailey, Janet"><span class="vcard"><span class="fn"><a href="/wiki/Janet_Dailey" title="Janet Dailey">Janet Dailey</a></span></span></span>
</td>
<td>300 million<sup id="cite_ref-52" class="reference"><a href="#cite_note-52">[52]</a></sup>
</td>
<td>300 million<sup id="cite_ref-53" class="reference"><a href="#cite_note-53">[53]</a></sup>
</td>
<td>English
</td>
<td>Romance
</td>
<td>93
</td>
<td>American
</td></tr>
<tr>
<td><span data-sort-value="Ludlum, Robert"><span class="vcard"><span class="fn"><a href="/wiki/Robert_Ludlum" title="Robert Ludlum">Robert Ludlum</a></span></span></span>
</td>
<td>110 million<sup id="cite_ref-54" class="reference"><a href="#cite_note-54">[54]</a></sup>
</td>
<td>290 million<sup id="cite_ref-55" class="reference"><a href="#cite_note-55">[55]</a></sup>
</td>
<td>English
</td>
<td><a href="/wiki/Thriller_(genre)" title="Thriller (genre)">Espionage</a>, <i><a href="/wiki/Jason_Bourne_(character)" class="mw-redirect" title="Jason Bourne (character)">Jason Bourne</a></i>
</td>
<td>40
</td>
<td>American
</td></tr>
<tr>
<td><span data-sort-value="Toriyama, Akira"><span class="vcard"><span class="fn"><a href="/wiki/Akira_Toriyama" title="Akira Toriyama">Akira Toriyama</a></span></span></span>
</td>
<td>
</td>
<td>287<span class="nowrap">&nbsp;</span>million<sup id="cite_ref-69" class="reference"><a href="#cite_note-69">[b]</a></sup>
</td>
<td>Japanese
</td>
<td><a href="/wiki/Manga" title="Manga">Manga</a>, <i><a href="/wiki/Dr._Slump" title="Dr. Slump">Dr. Slump</a></i>, <i><a href="/wiki/Dragon_Ball_(manga)" title="Dragon Ball (manga)">Dragon Ball</a></i>, <i><a href="/wiki/Dragon_Ball_Super" title="Dragon Ball Super">Dragon Ball Super</a></i>
</td>
<td>66
</td>
<td>Japanese
</td></tr>
<tr>
<td><span data-sort-value="Tezuka, Osamu"><span class="vcard"><span class="fn"><a href="/wiki/Osamu_Tezuka" title="Osamu Tezuka">Osamu Tezuka</a></span></span></span>
</td>
<td>
</td>
<td>276<span class="nowrap">&nbsp;</span>million<sup id="cite_ref-70" class="reference"><a href="#cite_note-70">[68]</a></sup>
</td>
<td>Japanese
</td>
<td><a href="/wiki/Manga" title="Manga">Manga</a>, <i><a href="/wiki/Astro_Boy" title="Astro Boy">Astro Boy</a></i>, <i><a href="/wiki/Black_Jack_(manga)" title="Black Jack (manga)">Black Jack</a></i>, <i><a href="/wiki/Buddha_(manga)" title="Buddha (manga)">Buddha</a></i>
</td>
<td>62
</td>
<td>Japanese
</td></tr>
<tr>
<td><span data-sort-value="Patterson, James"><span class="vcard"><span class="fn"><a href="/wiki/James_Patterson" title="James Patterson">James Patterson</a></span></span></span>
</td>
<td>150 million<sup id="cite_ref-71" class="reference"><a href="#cite_note-71">[69]</a></sup>
</td>
<td>275 million<sup id="cite_ref-72" class="reference"><a href="#cite_note-72">[70]</a></sup>
</td>
<td>English
</td>
<td><a href="/wiki/Thriller_fiction" class="mw-redirect" title="Thriller fiction">Thriller</a>, <i><a href="/wiki/Alex_Cross" title="Alex Cross">Alex Cross</a></i>
</td>
<td>98
</td>
<td>American
</td></tr>
<tr>
<td><span data-sort-value="Dard, Frédéric"><span class="vcard"><span class="fn"><a href="/wiki/Fr%C3%A9d%C3%A9ric_Dard" title="Frédéric Dard">Frédéric Dard</a></span></span></span>
</td>
<td>200 million<sup id="cite_ref-73" class="reference"><a href="#cite_note-73">[71]</a></sup>
</td>
<td>270 million<sup id="cite_ref-74" class="reference"><a href="#cite_note-74">[72]</a></sup>
</td>
<td>French
</td>
<td>Detective, <i>San Antonio</i>
</td>
<td>300
</td>
<td><a href="/wiki/French_people" title="French people">French</a>
</td></tr>
<tr>
<td><span data-sort-value="Berenstain, Stan and Jan"><span class="vcard"><span class="fn"><a href="/wiki/Stan_and_Jan_Berenstain" title="Stan and Jan Berenstain">Stan and Jan Berenstain</a></span></span></span>
</td>
<td>200 million<sup id="cite_ref-75" class="reference"><a href="#cite_note-75">[73]</a></sup>
</td>
<td>260 million<sup id="cite_ref-76" class="reference"><a href="#cite_note-76">[74]</a></sup>
</td>
<td>English
</td>
<td><i><a href="/wiki/Berenstain_Bears" title="Berenstain Bears">Berenstain Bears</a></i>
</td>
<td>300+
</td>
<td>American
</td></tr>
<tr>
<td><span data-sort-value="Dahl, Roald"><span class="vcard"><span class="fn"><a href="/wiki/Roald_Dahl" title="Roald Dahl">Roald Dahl</a></span></span></span>
</td>
<td>200 million<sup id="cite_ref-77" class="reference"><a href="#cite_note-77">[75]</a></sup>
</td>
<td>250 million<sup id="cite_ref-78" class="reference"><a href="#cite_note-78">[76]</a></sup>
</td>
<td>English
</td>
<td>Children's literature
</td>
<td>50
</td>
<td>British
</td></tr>
<tr>
<td><span data-sort-value="Grisham, John"><span class="vcard"><span class="fn"><a href="/wiki/John_Grisham" title="John Grisham">John Grisham</a></span></span></span>
</td>
<td>100 million<sup id="cite_ref-79" class="reference"><a href="#cite_note-79">[77]</a></sup>
</td>
<td>250 million<sup id="cite_ref-80" class="reference"><a href="#cite_note-80">[78]</a></sup>
</td>
<td>English
</td>
<td><a href="/wiki/Legal_thriller" title="Legal thriller">Legal thriller</a>
</td>
<td>22
</td>
<td>American
</td></tr>
<tr>
<td><span data-sort-value="Grey, Zane"><span class="vcard"><span class="fn"><a href="/wiki/Zane_Grey" title="Zane Grey">Zane Grey</a></span></span></span>
</td>
<td>
</td>
<td>250 million<sup id="cite_ref-81" class="reference"><a href="#cite_note-81">[79]</a></sup>
</td>
<td>English
</td>
<td>Western
</td>
<td>
</td>
<td>American
</td></tr>
<tr>
<td><span data-sort-value="Wallace, Irving"><span class="vcard"><span class="fn"><a href="/wiki/Irving_Wallace" title="Irving Wallace">Irving Wallace</a></span></span></span>
</td>
<td>
</td>
<td>250 million<sup id="cite_ref-82" class="reference"><a href="#cite_note-82">[80]</a></sup>
</td>
<td>English
</td>
<td><a href="/wiki/Suspense" title="Suspense">Suspense</a>
</td>
<td>
</td>
<td>American
</td></tr>
<tr>
<td><span data-sort-value="Tolkien, J. R. R."><span class="vcard"><span class="fn"><a href="/wiki/J._R._R._Tolkien" title="J. R. R. Tolkien">J. R. R. Tolkien</a></span></span></span>
</td>
<td>200 million<sup id="cite_ref-83" class="reference"><a href="#cite_note-83">[81]</a></sup>
</td>
<td>250 million<sup id="cite_ref-84" class="reference"><a href="#cite_note-84">[82]</a></sup>
</td>
<td>English
</td>
<td><i><a href="/wiki/The_Lord_of_the_Rings" title="The Lord of the Rings">The Lord of the Rings</a></i>, <i><a href="/wiki/The_Hobbit" title="The Hobbit">The Hobbit</a></i>, classical fantasy
</td>
<td>36
</td>
<td><a href="/wiki/Kingdom_of_England" title="Kingdom of England">English</a>
</td></tr>
<tr>
<td><span data-sort-value="Kishimoto, Masashi"><span class="vcard"><span class="fn"><a href="/wiki/Masashi_Kishimoto" title="Masashi Kishimoto">Masashi Kishimoto</a></span></span></span>
</td>
<td>
</td>
<td>235<span class="nowrap">&nbsp;</span>million<sup id="cite_ref-85" class="reference"><a href="#cite_note-85">[83]</a></sup>
</td>
<td>Japanese
</td>
<td><a href="/wiki/Manga" title="Manga">Manga</a>, <i><a href="/wiki/Naruto" title="Naruto">Naruto</a></i>
</td>
<td>72
</td>
<td>Japanese
</td></tr>
<tr>
<td><span data-sort-value="May, Karl"><span class="vcard"><span class="fn"><a href="/wiki/Karl_May" title="Karl May">Karl May</a></span></span></span>
</td>
<td>100 million<sup id="cite_ref-86" class="reference"><a href="#cite_note-86">[84]</a></sup>
</td>
<td>200 million<sup id="cite_ref-87" class="reference"><a href="#cite_note-87">[85]</a></sup>
</td>
<td><a href="/wiki/German_language" title="German language">German</a>
</td>
<td>Western, adventure
</td>
<td>80
</td>
<td><a href="/wiki/Germany" title="Germany">German</a>
</td></tr>
<tr>
<td><span data-sort-value="Brown, Carter"><span class="vcard"><span class="fn"><a href="/wiki/Carter_Brown" title="Carter Brown">Carter Brown</a></span></span></span>
</td>
<td>100 million<sup id="cite_ref-88" class="reference"><a href="#cite_note-88">[86]</a></sup>
</td>
<td>120 million<sup id="cite_ref-89" class="reference"><a href="#cite_note-89">[87]</a></sup>
</td>
<td>English
</td>
<td>Detective
</td>
<td>
</td>
<td>Australian
</td></tr>
<tr>
<td><span data-sort-value="Spillane, Mickey"><span class="vcard"><span class="fn"><a href="/wiki/Mickey_Spillane" title="Mickey Spillane">Mickey Spillane</a></span></span></span>
</td>
<td>100 million<sup id="cite_ref-90" class="reference"><a href="#cite_note-90">[88]</a></sup>
</td>
<td>200 million<sup id="cite_ref-91" class="reference"><a href="#cite_note-91">[89]</a></sup>
</td>
<td>English
</td>
<td>Detective, <i><a href="/wiki/Mike_Hammer" title="Mike Hammer">Mike Hammer</a></i>
</td>
<td>
</td>
<td>American
</td></tr>
<tr>
<td><span data-sort-value="Lewis, C. S."><span class="vcard"><span class="fn"><a href="/wiki/C._S._Lewis" title="C. S. Lewis">C. S. Lewis</a></span></span></span>
</td>
<td>100 million<sup id="cite_ref-92" class="reference"><a href="#cite_note-92">[90]</a></sup>
</td>
<td>200 million<sup id="cite_ref-93" class="reference"><a href="#cite_note-93">[91]</a></sup>
</td>
<td>English
</td>
<td><i><a href="/wiki/The_Chronicles_of_Narnia" title="The Chronicles of Narnia">The Chronicles of Narnia</a></i>, fantasy, popular theology
</td>
<td>38
</td>
<td>British
</td></tr>
<tr>
<td><span data-sort-value="Nishimura, Kyotaro"><span class="vcard"><span class="fn"><a href="/wiki/Kyotaro_Nishimura" title="Kyotaro Nishimura">Kyotaro Nishimura</a></span></span></span>
</td>
<td>
</td>
<td>200 million<sup id="cite_ref-94" class="reference"><a href="#cite_note-94">[92]</a></sup>
</td>
<td>Japanese
</td>
<td>Mystery
</td>
<td>400+
</td>
<td>Japanese
</td></tr>
<tr>
<td><span data-sort-value="Adachi, Mitsuru"><span class="vcard"><span class="fn"><a href="/wiki/Mitsuru_Adachi" title="Mitsuru Adachi">Mitsuru Adachi</a></span></span></span>
</td>
<td>
</td>
<td>200 million<sup id="cite_ref-mantan_rumiko_95-0" class="reference"><a href="#cite_note-mantan_rumiko-95">[93]</a></sup>
</td>
<td>Japanese
</td>
<td><a href="/wiki/Manga" title="Manga">Manga</a>, <i><a href="/wiki/Touch_(manga)" title="Touch (manga)">Touch</a></i>, <i><a href="/wiki/H2_(manga)" title="H2 (manga)">H2</a></i>, <i><a href="/wiki/Slow_Step" title="Slow Step">Slow Step</a></i>, <i><a href="/wiki/Miyuki_(manga)" title="Miyuki (manga)">Miyuki</a></i>,<i><a href="/wiki/Cross_Game" title="Cross Game">Cross Game</a></i>
</td>
<td>
</td>
<td>Japanese
</td></tr>
<tr>
<td><span data-sort-value="Takahashi, Rumiko"><span class="vcard"><span class="fn"><a href="/wiki/Rumiko_Takahashi" title="Rumiko Takahashi">Rumiko Takahashi</a></span></span></span>
</td>
<td>
</td>
<td>200 million<sup id="cite_ref-mantan_rumiko_95-1" class="reference"><a href="#cite_note-mantan_rumiko-95">[93]</a></sup>
</td>
<td>Japanese
</td>
<td><a href="/wiki/Manga" title="Manga">Manga</a> <i><a href="/wiki/Urusei_Yatsura" title="Urusei Yatsura">Urusei Yatsura</a></i>, <i><a href="/wiki/Ranma_%C2%BD" title="Ranma ½">Ranma ½</a></i>, <i><a href="/wiki/Inuyasha" title="Inuyasha">Inuyasha</a></i>, <i><a href="/wiki/Maison_Ikkoku" title="Maison Ikkoku">Maison Ikkoku</a></i>, <i><a href="/wiki/Rin-ne" title="Rin-ne">Rin-ne</a></i>
</td>
<td>
</td>
<td>Japanese
</td></tr>
<tr>
<td><span data-sort-value="Aoyama, Gosho"><span class="vcard"><span class="fn"><a href="/wiki/Gosho_Aoyama" title="Gosho Aoyama">Gosho Aoyama</a></span></span></span>
</td>
<td>
</td>
<td>200 million<sup id="cite_ref-96" class="reference"><a href="#cite_note-96">[94]</a></sup>
</td>
<td>Japanese
</td>
<td><a href="/wiki/Manga" title="Manga">Manga</a>, <i><a href="/wiki/Case_Closed_(manga)" class="mw-redirect" title="Case Closed (manga)">Detective Conan (Case Closed)</a></i>, <i><a href="/wiki/Yaiba" title="Yaiba">Yaiba</a></i>, <i><a href="/wiki/Magic_Kaito" title="Magic Kaito">Magic Kaito</a></i>
</td>
<td>
</td>
<td>Japanese
</td></tr>
<tr>
<td><span data-sort-value="Brown, Dan"><span class="vcard"><span class="fn"><a href="/wiki/Dan_Brown" title="Dan Brown">Dan Brown</a></span></span></span>
</td>
<td>200 million
</td>
<td>200 million<sup id="cite_ref-97" class="reference"><a href="#cite_note-97">[95]</a></sup>
</td>
<td>English
</td>
<td><a href="/wiki/Thriller_(genre)" title="Thriller (genre)">Thriller</a>, <i><a href="/wiki/Robert_Langdon" title="Robert Langdon">Robert Langdon</a></i>
</td>
<td>7<sup id="cite_ref-98" class="reference"><a href="#cite_note-98">[96]</a></sup>
</td>
<td>American
</td></tr>
<tr>
<td><span data-sort-value="Martin, Ann M."><span class="vcard"><span class="fn"><a href="/wiki/Ann_M._Martin" title="Ann M. Martin">Ann M. Martin</a></span></span></span>
</td>
<td>172 million<sup id="cite_ref-99" class="reference"><a href="#cite_note-99">[97]</a></sup>
</td>
<td>180 million<sup id="cite_ref-100" class="reference"><a href="#cite_note-100">[98]</a></sup>
</td>
<td>English
</td>
<td><i><a href="/wiki/The_Baby-sitters_Club" class="mw-redirect" title="The Baby-sitters Club">The Baby-sitters Club</a></i>
</td>
<td>335
</td>
<td>American
</td></tr>
<tr>
<td><span data-sort-value="Shiba, Ryōtarō"><span class="vcard"><span class="fn"><a href="/wiki/Ry%C5%8Dtar%C5%8D_Shiba" title="Ryōtarō Shiba">Ryōtarō Shiba</a></span></span></span>
</td>
<td>
</td>
<td>180 million<sup id="cite_ref-101" class="reference"><a href="#cite_note-101">[99]</a></sup>
</td>
<td>Japanese
</td>
<td><a href="/wiki/Historical_fiction" title="Historical fiction">Historical</a>
</td>
<td>350
</td>
<td>Japanese
</td></tr>
<tr>
<td><span data-sort-value="Hailey, Arthur"><span class="vcard"><span class="fn"><a href="/wiki/Arthur_Hailey" title="Arthur Hailey">Arthur Hailey</a></span></span></span>
</td>
<td>150 million<sup id="cite_ref-102" class="reference"><a href="#cite_note-102">[100]</a></sup>
</td>
<td>170 million<sup id="cite_ref-103" class="reference"><a href="#cite_note-103">[101]</a></sup>
</td>
<td>English
</td>
<td><a href="/wiki/Thriller_fiction" class="mw-redirect" title="Thriller fiction">Thriller</a>
</td>
<td>11
</td>
<td>British/Canadian
</td></tr>
<tr>
<td><span data-sort-value="Rice, Anne"><span class="vcard"><span class="fn"><a href="/wiki/Anne_Rice" title="Anne Rice">Anne Rice</a></span></span></span>
</td>
<td>150 million
</td>
<td>150 million+<sup id="cite_ref-104" class="reference"><a href="#cite_note-104">[102]</a></sup>
</td>
<td>English
</td>
<td>Gothic fiction, <a href="/wiki/Vampire_literature" title="Vampire literature">vampires</a>, <i><a href="/wiki/Interview_with_the_Vampire" title="Interview with the Vampire">Interview with the Vampire</a></i> (<i><a href="/wiki/The_Vampire_Chronicles" title="The Vampire Chronicles">The Vampire Chronicles</a></i>) <i><a href="/wiki/The_Witching_Hour_(novel)" class="mw-redirect" title="The Witching Hour (novel)">The Witching Hour</a></i> (<i><a href="/wiki/Lives_of_the_Mayfair_Witches" title="Lives of the Mayfair Witches">Lives of the Mayfair Witches</a></i>)
</td>
<td>40
</td>
<td>American
</td></tr>
<tr>
<td><span data-sort-value="Villiers, Gérard de"><span class="vcard"><span class="fn"><a href="/wiki/G%C3%A9rard_de_Villiers" title="Gérard de Villiers">Gérard de Villiers</a></span></span></span>
</td>
<td>
</td>
<td>150 million<sup id="cite_ref-105" class="reference"><a href="#cite_note-105">[103]</a></sup>
</td>
<td>French
</td>
<td>Detectives, <i>SAS</i>
</td>
<td>170
</td>
<td><a href="/wiki/France" title="France">French</a>
</td></tr>
<tr>
<td><span data-sort-value="Potter, Beatrix"><span class="vcard"><span class="fn"><a href="/wiki/Beatrix_Potter" title="Beatrix Potter">Beatrix Potter</a></span></span></span>
</td>
<td>100 million<sup id="cite_ref-106" class="reference"><a href="#cite_note-106">[104]</a></sup>
</td>
<td>150 million<sup id="cite_ref-107" class="reference"><a href="#cite_note-107">[105]</a></sup>
</td>
<td>English
</td>
<td><i><a href="/wiki/Peter_Rabbit" title="Peter Rabbit">Peter Rabbit</a></i>
</td>
<td>23
</td>
<td><a href="/wiki/Kingdom_of_England" title="Kingdom of England">English</a>
</td></tr>
<tr>
<td><span data-sort-value="Crichton, Michael"><span class="vcard"><span class="fn"><a href="/wiki/Michael_Crichton" title="Michael Crichton">Michael Crichton</a></span></span></span>
</td>
<td>150 million<sup id="cite_ref-108" class="reference"><a href="#cite_note-108">[106]</a></sup>
</td>
<td>150 million<sup id="cite_ref-109" class="reference"><a href="#cite_note-109">[107]</a></sup>
</td>
<td>English
</td>
<td><a href="/wiki/Thriller_fiction" class="mw-redirect" title="Thriller fiction">Techno thriller</a>
</td>
<td>25
</td>
<td>American
</td></tr>
<tr>
<td><span data-sort-value="Scarry, Richard"><span class="vcard"><span class="fn"><a href="/wiki/Richard_Scarry" title="Richard Scarry">Richard Scarry</a></span></span></span>
</td>
<td>100 million<sup id="cite_ref-110" class="reference"><a href="#cite_note-110">[108]</a></sup>
</td>
<td>150 million<sup id="cite_ref-111" class="reference"><a href="#cite_note-111">[109]</a></sup>
</td>
<td>English
</td>
<td>Illustrated children's books
</td>
<td>250
</td>
<td>American
</td></tr>
<tr>
<td><span data-sort-value="Cussler, Clive"><span class="vcard"><span class="fn"><a href="/wiki/Clive_Cussler" title="Clive Cussler">Clive Cussler</a></span></span></span>
</td>
<td>40 million<sup id="cite_ref-112" class="reference"><a href="#cite_note-112">[110]</a></sup>
</td>
<td>150 million<sup id="cite_ref-113" class="reference"><a href="#cite_note-113">[111]</a></sup>
</td>
<td>English
</td>
<td>Adventure, <i><a href="/wiki/Dirk_Pitt" title="Dirk Pitt">Dirk Pitt</a></i>
</td>
<td>37
</td>
<td>American
</td></tr>
<tr>
<td><span data-sort-value="MacLean, Alistair"><span class="vcard"><span class="fn"><a href="/wiki/Alistair_MacLean" title="Alistair MacLean">Alistair MacLean</a></span></span></span>
</td>
<td>150 million<sup id="cite_ref-114" class="reference"><a href="#cite_note-114">[112]</a></sup>
</td>
<td>200 million<sup id="cite_ref-115" class="reference"><a href="#cite_note-115">[113]</a></sup>
</td>
<td>English
</td>
<td>Adventure, thriller, <a href="/wiki/War_novel" title="War novel">war stories</a>
</td>
<td>32
</td>
<td>British
</td></tr>
<tr>
<td><span data-sort-value="Follett, Ken"><span class="vcard"><span class="fn"><a href="/wiki/Ken_Follett" title="Ken Follett">Ken Follett</a></span></span></span>
</td>
<td>90 million<sup id="cite_ref-116" class="reference"><a href="#cite_note-116">[114]</a></sup>
</td>
<td>150 million<sup id="cite_ref-117" class="reference"><a href="#cite_note-117">[115]</a></sup>
</td>
<td>English
</td>
<td><a href="/wiki/Thriller_fiction" class="mw-redirect" title="Thriller fiction">Spy thriller</a>, <a href="/wiki/Historical_fiction" title="Historical fiction">historical thriller</a>
</td>
<td>30
</td>
<td>British
</td></tr>
<tr>
<td><span data-sort-value="Lindgren, Astrid"><span class="vcard"><span class="fn"><a href="/wiki/Astrid_Lindgren" title="Astrid Lindgren">Astrid Lindgren</a></span></span></span>
</td>
<td>100 million<sup id="cite_ref-118" class="reference"><a href="#cite_note-118">[116]</a></sup>
</td>
<td>165 million<sup id="cite_ref-119" class="reference"><a href="#cite_note-119">[117]</a></sup>
</td>
<td><a href="/wiki/Swedish_language" title="Swedish language">Swedish</a>
</td>
<td>Children's literature
</td>
<td>100
</td>
<td><a href="/wiki/Sweden" title="Sweden">Swedish</a>
</td></tr>
<tr>
<td><span data-sort-value="Macomber, Debbie"><span class="vcard"><span class="fn"><a href="/wiki/Debbie_Macomber" title="Debbie Macomber">Debbie Macomber</a></span></span></span>
</td>
<td>60 million<sup id="cite_ref-120" class="reference"><a href="#cite_note-120">[118]</a></sup>
</td>
<td>140 million<sup id="cite_ref-121" class="reference"><a href="#cite_note-121">[119]</a></sup>
</td>
<td>English
</td>
<td>Romance
</td>
<td>
</td>
<td>American
</td></tr>
<tr>
<td><a href="/wiki/E._L._James" title="E. L. James">EL James</a>
</td>
<td>100 million
</td>
<td>125 million
</td>
<td>English
</td>
<td><i><a href="/wiki/Fifty_Shades_of_Grey" title="Fifty Shades of Grey">Fifty Shades of Grey</a></i>
</td>
<td>3
</td>
<td>British
</td></tr>
<tr>
<td><a href="/wiki/Tite_Kubo" title="Tite Kubo">Tite Kubo</a>
</td>
<td>
</td>
<td>120 million<sup id="cite_ref-122" class="reference"><a href="#cite_note-122">[120]</a></sup>
</td>
<td>Japanese
</td>
<td><a href="/wiki/Manga" title="Manga">Manga</a>, <i><a href="/wiki/Bleach_(manga)" title="Bleach (manga)">Bleach</a></i>
</td>
<td>74
</td>
<td>Japanese
</td></tr>
<tr>
<td><span data-sort-value="Yoshikawa, Eiji"><span class="vcard"><span class="fn"><a href="/wiki/Eiji_Yoshikawa" title="Eiji Yoshikawa">Eiji Yoshikawa</a></span></span></span>
</td>
<td>
</td>
<td>120 million<sup id="cite_ref-123" class="reference"><a href="#cite_note-123">[121]</a></sup>
</td>
<td>Japanese
</td>
<td><i><a href="/wiki/Musashi_(novel)" title="Musashi (novel)">Musashi</a></i>
</td>
<td>7
</td>
<td>Japanese
</td></tr>
<tr>
<td><span data-sort-value="Cookson, Catherine"><span class="vcard"><span class="fn"><a href="/wiki/Catherine_Cookson" title="Catherine Cookson">Catherine Cookson</a></span></span></span>
</td>
<td>100 million<sup id="cite_ref-124" class="reference"><a href="#cite_note-124">[122]</a></sup>
</td>
<td>120 million<sup id="cite_ref-125" class="reference"><a href="#cite_note-125">[123]</a></sup>
</td>
<td>English
</td>
<td>Romance
</td>
<td>103
</td>
<td>British
</td></tr>
<tr>
<td><span data-sort-value="Meyer, Stephenie"><span class="vcard"><span class="fn"><a href="/wiki/Stephenie_Meyer" title="Stephenie Meyer">Stephenie Meyer</a></span></span></span>
</td>
<td>100 million<sup id="cite_ref-126" class="reference"><a href="#cite_note-126">[124]</a></sup>
</td>
<td>116 million<sup id="cite_ref-127" class="reference"><a href="#cite_note-127">[125]</a></sup>
</td>
<td>English
</td>
<td><i><a href="/wiki/Twilight_(novel_series)" title="Twilight (novel series)">The Twilight Saga</a></i>, <i><a href="/wiki/The_Host_(novel)" title="The Host (novel)">The Host</a></i>, romance
</td>
<td>6
</td>
<td>American
</td></tr>
<tr>
<td><span data-sort-value="Bridwell, Norman"><span class="vcard"><span class="fn"><a href="/wiki/Norman_Bridwell" title="Norman Bridwell">Norman Bridwell</a></span></span></span>
</td>
<td>100 million<sup id="cite_ref-128" class="reference"><a href="#cite_note-128">[126]</a></sup>
</td>
<td>110 million<sup id="cite_ref-129" class="reference"><a href="#cite_note-129">[127]</a></sup>
</td>
<td>English
</td>
<td><i><a href="/wiki/Clifford_the_Big_Red_Dog" title="Clifford the Big Red Dog">Clifford the Big Red Dog</a></i>
</td>
<td>80
</td>
<td>American
</td></tr>
<tr>
<td><span data-sort-value="Baldacci, David"><span class="vcard"><span class="fn"><a href="/wiki/David_Baldacci" title="David Baldacci">David Baldacci</a></span></span></span>
</td>
<td>
</td>
<td>110 million<sup id="cite_ref-130" class="reference"><a href="#cite_note-130">[128]</a></sup>
</td>
<td>English
</td>
<td>Thriller
</td>
<td>25
</td>
<td>American
</td></tr>
<tr>
<td><a href="/wiki/Nicholas_Sparks" title="Nicholas Sparks">Nicholas Sparks</a>
</td>
<td>90 million<sup id="cite_ref-131" class="reference"><a href="#cite_note-131">[129]</a></sup>
</td>
<td>105 million<sup id="cite_ref-132" class="reference"><a href="#cite_note-132">[130]</a></sup>
</td>
<td>English
</td>
<td>Romance
</td>
<td>22
</td>
<td>American
</td></tr>
<tr>
<td><span data-sort-value="Araki, Hirohiko"><span class="vcard"><span class="fn"><a href="/wiki/Hirohiko_Araki" title="Hirohiko Araki">Hirohiko Araki</a></span></span></span>
</td>
<td>
</td>
<td>100 million<sup id="cite_ref-133" class="reference"><a href="#cite_note-133">[131]</a></sup>
</td>
<td>Japanese
</td>
<td><a href="/wiki/Manga" title="Manga">Manga</a>, <i><a href="/wiki/Jojo%27s_Bizarre_Adventure" class="mw-redirect" title="Jojo's Bizarre Adventure">Jojo's Bizarre Adventure</a></i>
</td>
<td>
</td>
<td>Japanese
</td></tr>
<tr>
<td><span data-sort-value="Hunter, Evan"><span class="vcard"><span class="fn"><a href="/wiki/Evan_Hunter" class="mw-redirect" title="Evan Hunter">Evan Hunter</a></span></span></span>
</td>
<td>100 million<sup id="cite_ref-134" class="reference"><a href="#cite_note-134">[132]</a></sup>
</td>
<td>100 million<sup id="cite_ref-135" class="reference"><a href="#cite_note-135">[133]</a></sup>
</td>
<td>English
</td>
<td>Detective (Ed McBain)
</td>
<td>94
</td>
<td>American
</td></tr>
<tr>
<td><span data-sort-value="Neiderman, Andrew"><span class="vcard"><span class="fn"><a href="/wiki/Andrew_Neiderman" title="Andrew Neiderman">Andrew Neiderman</a></span></span></span>
</td>
<td>100 million<sup id="cite_ref-136" class="reference"><a href="#cite_note-136">[134]</a></sup>
</td>
<td>100 million<sup id="cite_ref-137" class="reference"><a href="#cite_note-137">[135]</a></sup>
</td>
<td>English
</td>
<td><a href="/wiki/V._C._Andrews" title="V. C. Andrews">V. C. Andrews</a>, <i>The Devil's Advocate</i>
</td>
<td>60
</td>
<td>American
</td></tr>
<tr>
<td><span data-sort-value="Hargreaves, Roger"><span class="vcard"><span class="fn"><a href="/wiki/Roger_Hargreaves" title="Roger Hargreaves">Roger Hargreaves</a></span></span></span>
</td>
<td>100 million<sup id="cite_ref-138" class="reference"><a href="#cite_note-138">[136]</a></sup>
</td>
<td>100 million<sup id="cite_ref-139" class="reference"><a href="#cite_note-139">[137]</a></sup>
</td>
<td>English
</td>
<td>Children's literature, <i><a href="/wiki/Mr._Men" title="Mr. Men">Mr. Men</a></i>
</td>
<td>
</td>
<td>British
</td></tr>
<tr>
<td><span data-sort-value="Cook, Robin"><span class="vcard"><span class="fn"><a href="/wiki/Robin_Cook_(novelist)" class="mw-redirect" title="Robin Cook (novelist)">Robin Cook</a></span></span></span>
</td>
<td>100 million<sup id="cite_ref-140" class="reference"><a href="#cite_note-140">[138]</a></sup>
</td>
<td>100 million<sup id="cite_ref-141" class="reference"><a href="#cite_note-141">[139]</a></sup>
</td>
<td>English
</td>
<td><a href="/wiki/Thriller_fiction" class="mw-redirect" title="Thriller fiction">Medical thriller</a> <a href="/wiki/Coma_(novel)" title="Coma (novel)">Coma</a>
</td>
<td>27
</td>
<td>American
</td></tr>
<tr>
<td><span data-sort-value="Smith, Wilbur"><span class="vcard"><span class="fn"><a href="/wiki/Wilbur_Smith" title="Wilbur Smith">Wilbur Smith</a></span></span></span>
</td>
<td>80 million<sup id="cite_ref-142" class="reference"><a href="#cite_note-142">[140]</a></sup>
</td>
<td>100 million<sup id="cite_ref-143" class="reference"><a href="#cite_note-143">[141]</a></sup>
</td>
<td>English
</td>
<td>African adventure
</td>
<td>32
</td>
<td>South African/British
</td></tr>
<tr>
<td><span data-sort-value="Caldwell, Erskine"><span class="vcard"><span class="fn"><a href="/wiki/Erskine_Caldwell" title="Erskine Caldwell">Erskine Caldwell</a></span></span></span>
</td>
<td>80 million<sup id="cite_ref-144" class="reference"><a href="#cite_note-144">[142]</a></sup>
</td>
<td>100 million<sup id="cite_ref-145" class="reference"><a href="#cite_note-145">[143]</a></sup>
</td>
<td>English
</td>
<td>Literature
</td>
<td>25
</td>
<td>American
</td></tr>
<tr>
<td><a href="/wiki/Judith_Krantz" title="Judith Krantz">Judith Krantz</a>
</td>
<td>80 million <sup id="cite_ref-146" class="reference"><a href="#cite_note-146">[144]</a></sup>
</td>
<td>100 million <sup id="cite_ref-147" class="reference"><a href="#cite_note-147">[145]</a></sup>
</td>
<td>English
</td>
<td>Romance
</td>
<td>12
</td>
<td>American
</td></tr>
<tr>
<td><span data-sort-value="Hibbert, Eleanor"><span class="vcard"><span class="fn"><a href="/wiki/Eleanor_Hibbert" title="Eleanor Hibbert">Eleanor Hibbert</a></span></span></span>
</td>
<td>100 million<sup id="cite_ref-148" class="reference"><a href="#cite_note-148">[146]</a></sup>
</td>
<td>100 million<sup id="cite_ref-149" class="reference"><a href="#cite_note-149">[147]</a></sup>
</td>
<td>English
</td>
<td>Romance, historical, suspense
</td>
<td>200
</td>
<td>British
</td></tr>
<tr>
<td><span data-sort-value="Carroll, Lewis"><span class="vcard"><span class="fn"><a href="/wiki/Lewis_Carroll" title="Lewis Carroll">Lewis Carroll</a></span></span></span>
</td>
<td>
</td>
<td>100 million<sup id="cite_ref-150" class="reference"><a href="#cite_note-150">[148]</a></sup>
</td>
<td>English
</td>
<td><i><a href="/wiki/Alice%27s_Adventures_in_Wonderland" title="Alice's Adventures in Wonderland">Alice's Adventures in Wonderland</a></i>, absurdist literature
</td>
<td>5
</td>
<td>British
</td></tr>
<tr>
<td><span data-sort-value="Robins, Denise"><span class="vcard"><span class="fn"><a href="/wiki/Denise_Robins" title="Denise Robins">Denise Robins</a></span></span></span>
</td>
<td>
</td>
<td>100 million<sup id="cite_ref-151" class="reference"><a href="#cite_note-151">[149]</a></sup>
</td>
<td>English
</td>
<td>Romance
</td>
<td>200
</td>
<td>British
</td></tr>
<tr>
<td><span data-sort-value="Xueqin, Cao"><span class="vcard"><span class="fn"><a href="/wiki/Cao_Xueqin" title="Cao Xueqin">Cao Xueqin</a></span></span></span>
</td>
<td>
</td>
<td>100 million<sup id="cite_ref-152" class="reference"><a href="#cite_note-152">[150]</a></sup>
</td>
<td>Chinese
</td>
<td><i><a href="/wiki/Dream_of_the_Red_Chamber" title="Dream of the Red Chamber">Dream of the Red Chamber</a></i>
</td>
<td>
</td>
<td><a href="/wiki/China" title="China">Chinese</a>
</td></tr>
<tr>
<td><span data-sort-value="Fleming, Ian"><span class="vcard"><span class="fn"><a href="/wiki/Ian_Fleming" title="Ian Fleming">Ian Fleming</a></span></span></span>
</td>
<td>100 million<sup id="cite_ref-153" class="reference"><a href="#cite_note-153">[151]</a></sup>
</td>
<td>100 million<sup id="cite_ref-154" class="reference"><a href="#cite_note-154">[152]</a></sup>
</td>
<td>English
</td>
<td><i><a href="/wiki/James_Bond" title="James Bond">James Bond</a></i>
</td>
<td>14
</td>
<td>British
</td></tr>
<tr>
<td><span data-sort-value="Hesse, Hermann"><span class="vcard"><span class="fn"><a href="/wiki/Hermann_Hesse" title="Hermann Hesse">Hermann Hesse</a></span></span></span>
</td>
<td>100 million<sup id="cite_ref-155" class="reference"><a href="#cite_note-155">[153]</a></sup>
</td>
<td>100 million<sup id="cite_ref-156" class="reference"><a href="#cite_note-156">[154]</a></sup>
</td>
<td>German
</td>
<td><i><a href="/wiki/Steppenwolf_(novel)" title="Steppenwolf (novel)">Steppenwolf</a></i>, <i><a href="/wiki/Siddhartha_(novel)" title="Siddhartha (novel)">Siddhartha</a></i>, <i><a href="/wiki/The_Glass_Bead_Game" title="The Glass Bead Game">The Glass Bead Game</a></i>
</td>
<td>45
</td>
<td>German-Swiss
</td></tr>
<tr>
<td><span data-sort-value="Stout, Rex"><span class="vcard"><span class="fn"><a href="/wiki/Rex_Stout" title="Rex Stout">Rex Stout</a></span></span></span>
</td>
<td>100 million<sup id="cite_ref-157" class="reference"><a href="#cite_note-157">[155]</a></sup>
</td>
<td>100 million<sup id="cite_ref-158" class="reference"><a href="#cite_note-158">[156]</a></sup>
</td>
<td>English
</td>
<td><i><a href="/wiki/Nero_Wolfe" title="Nero Wolfe">Nero Wolfe</a></i>
</td>
<td>50
</td>
<td>American
</td></tr>
<tr>
<td><span data-sort-value="Golon, Anne"><span class="vcard"><span class="fn"><a href="/wiki/Anne_Golon" title="Anne Golon">Anne Golon</a></span></span></span>
</td>
<td>100 million<sup id="cite_ref-159" class="reference"><a href="#cite_note-159">[157]</a></sup>
</td>
<td>100 million<sup id="cite_ref-160" class="reference"><a href="#cite_note-160">[158]</a></sup>
</td>
<td>French
</td>
<td><i><a href="/wiki/Ang%C3%A9lique,_the_Marquise_of_the_Angels" title="Angélique, the Marquise of the Angels">Angélique</a></i>
</td>
<td>14
</td>
<td>French
</td></tr>
<tr>
<td><span data-sort-value="Slaughter, Frank G."><span class="vcard"><span class="fn"><a href="/wiki/Frank_G._Slaughter" title="Frank G. Slaughter">Frank G. Slaughter</a></span></span></span>
</td>
<td>
</td>
<td>100 million<sup id="cite_ref-161" class="reference"><a href="#cite_note-161">[159]</a></sup>
</td>
<td>English
</td>
<td>Medical
</td>
<td>62
</td>
<td>American
</td></tr>
<tr>
<td><span data-sort-value="Burroughs, Edgar Rice"><span class="vcard"><span class="fn"><a href="/wiki/Edgar_Rice_Burroughs" title="Edgar Rice Burroughs">Edgar Rice Burroughs</a></span></span></span>
</td>
<td>100 million<sup id="cite_ref-162" class="reference"><a href="#cite_note-162">[160]</a></sup>
</td>
<td>100 million<sup id="cite_ref-163" class="reference"><a href="#cite_note-163">[161]</a></sup>
</td>
<td>English
</td>
<td><i><a href="/wiki/Tarzan" title="Tarzan">Tarzan</a></i>, <i><a href="/wiki/Barsoom" title="Barsoom">Barsoom</a></i> and <i><a href="/wiki/Pellucidar" title="Pellucidar">Pellucidar</a></i> series, <a href="/wiki/Science_fantasy" title="Science fantasy">science fantasy</a>
</td>
<td>
</td>
<td>American
</td></tr>
<tr>
<td><span data-sort-value="Creasey, John"><span class="vcard"><span class="fn"><a href="/wiki/John_Creasey" title="John Creasey">John Creasey</a></span></span></span>
</td>
<td>
</td>
<td>100 million<sup id="cite_ref-164" class="reference"><a href="#cite_note-164">[162]</a></sup>
</td>
<td>English
</td>
<td>Crime thriller
</td>
<td>600
</td>
<td>British
</td></tr>
<tr>
<td><span data-sort-value="Michener, James A."><span class="vcard"><span class="fn"><a href="/wiki/James_A._Michener" title="James A. Michener">James A. Michener</a></span></span></span>
</td>
<td>
</td>
<td>100 million<sup id="cite_ref-165" class="reference"><a href="#cite_note-165">[163]</a></sup>
</td>
<td>English
</td>
<td>Historical
</td>
<td>47
</td>
<td>American
</td></tr>
<tr>
<td><span data-sort-value="Uchida, Yasuo"><span class="vcard"><span class="fn"><a href="/w/index.php?title=Yasuo_Uchida&amp;action=edit&amp;redlink=1" class="new" title="Yasuo Uchida (page does not exist)">Yasuo Uchida</a></span></span></span>
</td>
<td>
</td>
<td>100 million<sup id="cite_ref-shoten_166-0" class="reference"><a href="#cite_note-shoten-166">[164]</a></sup>
</td>
<td>Japanese
</td>
<td>Mystery
</td>
<td>130+
</td>
<td>Japanese
</td></tr>
<tr>
<td><span data-sort-value="Morimura, Seiichi"><span class="vcard"><span class="fn"><a href="/wiki/Seiichi_Morimura" title="Seiichi Morimura">Seiichi Morimura</a></span></span></span>
</td>
<td>
</td>
<td>100 million<sup id="cite_ref-shoten_166-1" class="reference"><a href="#cite_note-shoten-166">[164]</a></sup>
</td>
<td>Japanese
</td>
<td>Mystery
</td>
<td>350+
</td>
<td>Japanese
</td></tr>
<tr>
<td><span data-sort-value="Higgins Clark, Mary"><span class="vcard"><span class="fn"><a href="/wiki/Mary_Higgins_Clark" title="Mary Higgins Clark">Mary Higgins Clark</a></span></span></span>
</td>
<td>100 million<sup id="cite_ref-167" class="reference"><a href="#cite_note-167">[165]</a></sup>
</td>
<td>100 million<sup id="cite_ref-168" class="reference"><a href="#cite_note-168">[166]</a></sup>
</td>
<td>English
</td>
<td>Thriller
</td>
<td>
</td>
<td>American
</td></tr>
<tr>
<td><span data-sort-value="Jordan, Penny"><span class="vcard"><span class="fn"><a href="/wiki/Penny_Jordan" title="Penny Jordan">Penny Jordan</a></span></span></span>
</td>
<td>90 million<sup id="cite_ref-169" class="reference"><a href="#cite_note-169">[167]</a></sup>
</td>
<td>100 million<sup id="cite_ref-170" class="reference"><a href="#cite_note-170">[168]</a></sup>
</td>
<td>English
</td>
<td>Romance
</td>
<td>200+
</td>
<td>British
</td></tr>
<tr>
<td><span data-sort-value="Cornwell, Patricia"><span class="vcard"><span class="fn"><a href="/wiki/Patricia_Cornwell" title="Patricia Cornwell">Patricia Cornwell</a></span></span></span>
</td>
<td>
</td>
<td>100 million<sup id="cite_ref-171" class="reference"><a href="#cite_note-171">[169]</a></sup>
</td>
<td>English
</td>
<td>Thriller
</td>
<td>34+
</td>
<td>American
</td></tr>
<tr>
<td><span data-sort-value="Isayama, Hajime"><span class="vcard"><span class="fn"><a href="/wiki/Hajime_Isayama" title="Hajime Isayama">Hajime Isayama</a></span></span></span>
</td>
<td>100 million
</td>
<td>100 million<sup id="cite_ref-172" class="reference"><a href="#cite_note-172">[170]</a></sup>
</td>
<td><a href="/wiki/Japanese_language" title="Japanese language">Japanese</a>
</td>
<td><a href="/wiki/Manga" title="Manga">Manga</a>, <i><a href="/wiki/Attack_on_Titan" title="Attack on Titan">Attack on Titan</a></i>
</td>
<td>
</td>
<td><a href="/wiki/Japan" title="Japan">Japanese</a>
</td></tr></tbody>
"""

soup = BeautifulSoup(author, 'html.parser')
with open('authors.txt', 'w', encoding='utf-8') as f:
    for data in soup.find_all('tr'):
        f.write(data.find_all('td')[0].get_text().strip('\n'))
        f.write('\n')