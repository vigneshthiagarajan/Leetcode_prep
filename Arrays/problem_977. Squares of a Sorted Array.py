class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Simple sort
        squared = [i * i for i in nums]
        squared.sort()
        return squared

#         # Two pointer
#         negatives = [i for i in nums if i<0]
#         positives = [i for i in nums if i>=0]

#         negative_squares = [i*i for i in negatives]
#         positive_squares = [i*i for i in positives]
#         pointer_1 = len(negative_squares)-1
#         pointer_2 = 0
#         all_squares = []
#         while(pointer_1>=0 and pointer_2<len(positive_squares)):
#             if(negative_squares[pointer_1]<=positive_squares[pointer_2]):
#                 all_squares.append(negative_squares[pointer_1])
#                 pointer_1-=1
#             else:
#                 all_squares.append(positive_squares[pointer_2])
#                 pointer_2+=1
#         if(pointer_1 >= 0):
#             print(negative_squares[pointer_1::-1])
#             all_squares = all_squares + negative_squares[pointer_1::-1]
#         elif(pointer_2<len(positive_squares)):
#             all_squares = all_squares + positive_squares[pointer_2::1]


#        return all_squares