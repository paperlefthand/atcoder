main :: IO()
main = do
    num <- getLine
    putStrLn $ ans $ f (read num) []

f :: Int -> [Int] -> [Int]
f n xs | n < 10 = n : xs
       | n >= 10 = (n `mod` 10) : f (n `div` 10) xs

ans :: [Int] -> String
ans xs | reverse xs == xs = "Yes"
       | otherwise = "No"
