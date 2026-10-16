class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product1 = 1
        output1 = []
        product2 = 1
        output2 = []
        output_final = []

        for i in nums:
            output1.append(product1)
            product1 *= i

        for j in nums[::-1]:
            output2.append(product2)
            product2 *= j

        for index, l in enumerate(output2[::-1]):
            product_final = l * output1[index]
            output_final.append(product_final)

        return output_final