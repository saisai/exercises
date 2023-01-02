
function acc(init)
    init = init or 0
    return function(delta)
        init = init + (delta or 0)
        return init
    end
end

x = acc(1)
print(x)
acc(3)
print(x(2.3))
