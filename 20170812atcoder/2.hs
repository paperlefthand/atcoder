main :: IO()
main = do
    nums <- words <$> getLine
    let a = map read nums !! 0
    let b = map read nums !! 1
    let c = map read nums !! 2
    let d = map read nums !! 3
    putStrLn $ show $ max_ (0, (min_ (b,d) - max_ (a,c)))

max_ :: (Int,Int) -> Int
max_ (x,y) | x >= y = x
          | otherwise = y

min_ :: (Int,Int) -> Int
min_ (x,y) | x >= y = y
          | otherwise = x
