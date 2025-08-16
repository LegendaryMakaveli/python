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
	





















