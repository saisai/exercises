
-- For tables as simple arrays, use the # operator
fruits = {"apple", "orange"}
print(#fruits)

fruits = {fruit1 = "apple", fruit2 = "orage"}
print(#fruits)

function size(tab)
	local count = 0
	for k, v in pairs(tab) do
		count = count + 1
	end
	return count
end
print(size(fruits))


