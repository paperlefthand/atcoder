main :: IO()
main = do
    num <- getLine
    let t = times (read num) []
    putStrLn $ show $ lcm_s t

times :: Int -> [Int] -> [Int]
times 0 xs = xs
times n xs = do
    x <- getLine
    return $ times (n-1) (read x):xs

lcm_s :: [Int] -> Int
lcm_s (x:xs) | xs == [] = x
            | otherwise = lcm_s $ map (\a -> lcm_ (x,a)) xs

lcm_ :: (Int,Int) -> Int
lcm_ a b = divc ab [2..(ab `div` 2)]

divc :: Int -> [Int] -> Int
divc x [] = x
divc y (x:xs) | (y `mod` x) == 0 = divc (y `div` x) xs
              | otherwise = divc y xs
