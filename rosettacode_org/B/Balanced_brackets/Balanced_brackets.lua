function isBalanced(s)
    return s:gsub('%b[]', '')=='' and true or false
end

function randomString()
    math.randomseed(os.time())
    math.random()math.random()math.random()math.random()
    local tokes = {'[', ']'}
    local result ={}
    for i=1,8 do
        table.insert(result, tokes[math.random(1, 2)])
    end
    return table.concat(result)
end

local RS = randomString()
print(RS)
print(isBalanced(RS))
    
