f = (a, b) => {
    if(a === 0 || b === 0)
        return 0

    let r = a
    for(let i = 0; i < b - 1; i++)
        r += a

    return r
}

// f(5, 0) ==> 0
// f(5, 5) ==> 25
// f(200, 2) => 400
