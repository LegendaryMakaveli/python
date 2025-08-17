from unittest import TestCase
import prove_of_concept_on_collection



class TestForAddingNewNumberToTuple(TestCase) :
	def test_that_the_function_only_accept_tuple_and_length(makaveli) :
		result = prove_of_concept_on_collection.append_number_to_tuple((1,2,3,4), (9))
		makaveli.assertIsInstance(result,tuple)
		makaveli.assertEqual(len(result), 5)

	def test_that_no_float_in_tuple(makaveli) :
		makaveli.assertRaises(ValueError, prove_of_concept_on_collection.append_number_to_tuple, (1,2,3,4,5),(4.0,))



class TestForTheSumOfInnerListFunction(TestCase) :
	def test_the_function_only_accept_list(makaveli) :
		result = prove_of_concept_on_collection.sum_inner ([[1,2,3],[2,3,4]])
		makaveli.assertIsInstance(result, list)		

	def test_for_negative_input_in_the_function(makaveli) :
		makaveli.assertRaises(ValueError, prove_of_concept_on_collection.sum_inner, (-2,-1))

	def test_for_string_input_in_the_function(makaveli) :
		makaveli.assertRaises(ValueError, prove_of_concept_on_collection.sum_inner, (""))

	def test_if_the_function_work_perfectly(makaveli) :
		result = prove_of_concept_on_collection.sum_inner ([[1,2,3],[2,3,4]])
		makaveli.assertEqual(result, [6, 9])

	def test_for_the_confirm_functionality(makaveli) :
		result = prove_of_concept_on_collection.sum_inner ([[1,2,3],[2,3,4]])
		makaveli.assertNotEqual(result, [8, 9])



class TestForTheFilterOfAllEvenNumberInARange(TestCase) :
	def test_that_the_function_accpet_only_list(makaveli) :
		result = prove_of_concept_on_collection.return_even ([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
		makaveli.assertEqual(type(result), list)
		makaveli.assertEqual(len(result), 11)



class TestForTheFilterOfAllLetterLongerThan5InARange(TestCase) :
	def test_that_the_function_accpet_only_list(makaveli) :
		result = prove_of_concept_on_collection. return_letter_longer_than_five (["Cat", " Elephant", "Tiger", "Lion"])
		makaveli.assertEqual(type(result), list)
		makaveli.assertEqual(len(result), 1)

	def test_the_function_accept_no_int(makaveli) :
		with makaveli.assertRaises(ValueError) :
			 prove_of_concept_on_collection.return_letter_longer_than_five([2, 3])


class TestForTheFunctionThatFilterTheFirstValueGreaterThan2(TestCase) :
	def test_the_function_only_accept_list(makaveli) :
		result = prove_of_concept_on_collection.filter_first_value_greater_than_2 ([(1, 'A'), (4, 'B'), (2, 'C')])
		makaveli.assertIsInstance(result, list)

	def test_that_the_function_doesnt_accept_tuple(makaveli) :
		with makaveli.assertRaises(TypeError) :
			prove_of_concept_on_collection.filter_first_value_greater_than_2 (((1, 'A'), (4, 'B'), (2, 'C')))


	def test_for_function_functionality(makaveli) :
		result = prove_of_concept_on_collection.filter_first_value_greater_than_2 ([(1, 'A'), (4, 'B'), (2, 'C')])
		makaveli.assertEqual(result, [(4, 'B')])


class TestForNumberThatIsDivisibleBy3AndBy5(TestCase) :
	def test_for_Zero_and_negative_input(makaveli) :
		makaveli.assertRaises(ValueError, prove_of_concept_on_collection.is_range, 0)
	
	def test_for_negative_input(makaveli) :
		makaveli.assertRaises(ValueError,  prove_of_concept_on_collection.is_range, -1)

	def test_for_function_functionality(makaveli) :
		makaveli.assertTrue( prove_of_concept_on_collection.is_range (15))
		makaveli.assertFalse( prove_of_concept_on_collection.is_range (10))




class TestForFilteringAllNumberThatCanAreDivisibleBy3And5(TestCase) :
	def test_that_the_function_exist(makaveli) :
		prove_of_concept_on_collection.filter_numbers([1,2,3,4,5,6,7])

	def test_for_the_function_functionality(makaveli) :
		result = prove_of_concept_on_collection.filter_numbers([15,16,17,30,35,45,60,75,90,100,122,56])
		makaveli.assertEqual(result, [15,30,45,60,75,90])

	
class TestForPalindromeFromWordsFunction(TestCase) :
	def test_for_no_integers_in_the_function(makaveli) :
		makaveli.assertRaises(ValueError, prove_of_concept_on_collection.is_palindrome, 7)

	def test_for_Zero_input_in_the_function(makaveli) :
		makaveli.assertRaises(ValueError, prove_of_concept_on_collection.is_palindrome, 0)

	def test_for_negative_input_in_the_function(makaveli) :
		makaveli.assertRaises(ValueError, prove_of_concept_on_collection.is_palindrome, -1)

	def test_the_functon_functionality(makaveli) :
		result = prove_of_concept_on_collection.is_palindrome("madam")
		makaveli.assertNotEqual(result, "madam")


class TestForPalindrome(TestCase) :
	def test_that_the_function_only_accept_list(makaveli) :
		makaveli.assertTrue(prove_of_concept_on_collection.check_for_palindrome (["words", "levels", "madam"]))

	def test_for_no_integers_in_the_function(makaveli) :
		makaveli.assertRaises(ValueError, prove_of_concept_on_collection.check_for_palindrome, ([2,3,4]))

	def test_the_function_functionality(makaveli) :
		result = prove_of_concept_on_collection.check_for_palindrome, (["words", "level", "madam"])
		makaveli.assertNotEqual(result, ["level", "madam"])


class TestFunctionThatConvertStringsToUpperCase(TestCase) :	
	def test_that_the_function_only_accept_list(makaveli) :
		makaveli.assertTrue(prove_of_concept_on_collection.convert_to_upper (["word", "class"]))

	def test_that_the_function_accept_only_string(makaveli) :
		makaveli.assertRaises(ValueError, prove_of_concept_on_collection.convert_to_upper, ([2,3,4,5,6]))

	def test_the_function_functionality(makaveli) :
		result = prove_of_concept_on_collection.convert_to_upper (["hello", "world"])
		makaveli.assertEqual(result, ["HELLO", "WORLD"])


class TestFunctionThatSquareAllNumberInARange(TestCase) :
	def test_that_the_function_only_accept_list(makaveli) :
		makaveli.assertTrue(  prove_of_concept_on_collection.square_number ([1,2,3,4,5,6,7,8,9,10]))

	def test_that_the_function_dont_accept_anything_other_than_integers(makaveli) :
		makaveli.assertRaises(ValueError, prove_of_concept_on_collection.square_number, (["welcome", 56.99]))

	def test_the_function_functionality(makaveli) :
		result = prove_of_concept_on_collection.square_number([1,2,3,4,5]) 
		makaveli.assertEqual(result, [1,4,9,16,25])


class TestFunctionThatCaplitalizedTheFirstLetterInAString(TestCase) :
	def test_that_the_function_only_accept_list(makaveli) :
		makaveli.assertTrue(prove_of_concept_on_collection.capitalize_first_letter (["Hello", "World", "Python"]))

	def test_that_the_function_only_accept_strings(makaveli) :
		makaveli.assertRaises(ValueError, prove_of_concept_on_collection.capitalize_first_letter, ([2,3,4,5,78.45,9.5]))

	def test_the_function_functionality(makaveli) :
		result = prove_of_concept_on_collection.capitalize_first_letter (["hello", "world"])
		makaveli.assertEqual(result, ["Hello", "World"])
		makaveli.assertNotEqual(result, ["hello", "world"])

	
class TestFunctionThatAdd10PercentTax(TestCase) :
	def test_that_the_function_only_accept_list(makaveli) :
		makaveli.assertTrue(prove_of_concept_on_collection.add_tax ([100,200,300]))

	def test_that_the_function_only_accept_integers_and_float(makaveli) :
		makaveli.assertRaises(ValueError, prove_of_concept_on_collection.add_tax, (["Hello", "Wolrd"]))

	def test_the_function_functionality(makaveli) :
		result = prove_of_concept_on_collection.add_tax ([100,200,300])
		makaveli.assertNotEqual(result, [110.0, 220.0,330.0])


class TestFunctionThatSumNumberInARangeWithReduceMethod(TestCase) :
	def test_that_the_function_only_accept_list(makaveli) :
		makaveli.assertTrue(prove_of_concept_on_collection.sum_all_numbers ([1,2,3,4,5,6,7,8,9,10]))

	def test_that_the_function_only_accept_integers(makaveli) :
		makaveli.assertRaises(ValueError, prove_of_concept_on_collection.sum_all_numbers, (["Hello", 34.9, 34.333, "world"]))

	def test_the_function_functionality(makaveli) :
		result = prove_of_concept_on_collection.sum_all_numbers ([1,2,3,4,5]) 
		makaveli.assertEqual(result, 15)
























