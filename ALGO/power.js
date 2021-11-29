function power(a, b){
    var result = 1;
    
    if (b > 0)
    {
        for (var i = 1; i <= b; ++i)
        {
            result *= a;
        }
    }
    else if (b < 0)
    {
        for (var i = -1; i >= b; --i)
        {
            result /= a;
        }
    }
    
    return result;
    }
