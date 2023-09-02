--    This program is free software: you can redistribute it and/or modify
--    it under the terms of the GNU General Public License as published by
--    the Free Software Foundation, either version 3 of the License, or
--    (at your option) any later version.
--
--    This program is distributed in the hope that it will be useful,
--    but WITHOUT ANY WARRANTY; without even the implied warranty of
--    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
--    GNU General Public License for more details.
--
--    You should have received a copy of the GNU General Public License
--    along with this program.  If not, see <https://www.gnu.org/licenses/>.


awsome_protocol = Proto("AWSOME", "AWSOME PROTOCOL") 
X = ProtoField.uint8("AWSOME.Type", "Type", base.DEC)
B4 = ProtoField.uint32("AWSOME.B4", "B4", base.HEX)
B2 = ProtoField.uint16("AWSOME.B2", "B2", base.DEC)

awsome_protocol.fields = {X,B4, B2}

-- TUNNEL A MAC PACKET INSIDE AWESOME
function awsome_protocol.dissector(buffer, pinfo, tree)
    length = buffer:len();
    pinfo.cols.protocol = awsome_protocol.name
    local subtree = tree:add(awsome_protocol,buffer(), "AWSOME PROTOCOL DATA")
    local eth_withoutfcs = Dissector.get("eth_withoutfcs")
    subtree:add( X, buffer(0,1))
    if buffer(0,1):uint() == 0x0 then
		   subtree:add( B4, buffer(1,4))
		   eth_withoutfcs(buffer(5, length - 5):tvb(), pinfo, tree)
    else 
		   subtree:add( B2, buffer(1,2))
		   eth_withoutfcs(buffer(3, length - 3):tvb(), pinfo, tree)
    end

end

ether_table = DissectorTable.get("ethertype")
ether_table:add(0xdead, awsome_protocol)
ether_table:add(0xbeef, awsome_protocol)
