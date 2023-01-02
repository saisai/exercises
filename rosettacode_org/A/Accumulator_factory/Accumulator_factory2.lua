
do
    local accSum = 0
    function acc(v)
        accSum = accSum + (v or 0)

        local closuredSum = accSum
        return function(w)
            closuredSum = closuredSum + (w or 0)
            return closureSum
        end, accSum
    end
end

x = acc(1)
print(x)
x(5)
acc(3)
print(x(2.3))

