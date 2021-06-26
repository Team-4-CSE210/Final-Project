
class CheckMathProperty:
    """
    A code template for checking if the input math equation is correct.
    The responsibility of this class of objects is to
    update the game state when the user chooses items
    to match one of the math property's equation.

    Stereotype:
        Controller (?)

    Attributes:
        choice_list (list):  the equation submitted by the Player user.
    """

    def add_id(self, choice_list):
        """
        Method for Addition Identity Property: if correct, return True.

        Identity Property of Addition: 0 + A = A

        Args:
            cast (dict): the game actors {key: tag, value: list}.
        """
        if (choice_list[0] == 0 and
            # (AH) doesn't matter if chose number/letter or fruit.
            # not isinstance(choice_list[1], int) and
            choice_list[2] == choice_list[1]
            ):
            return True
        return False

    def add_commut(self, choice_list):
        """
        Method for Addition Commutative Property: if correct, return True.

        Commutative Property of Addition: A + B = B + A

        Args:
            cast (dict): the game actors {key: tag, value: list}.
        """

        if (choice_list[2] == choice_list[1] and
            choice_list[3] == choice_list[0]
            ):
            return True
        return False

    def add_assoc(self, choice_list):
        """
        Method for Addition Associative Property: if correct, return True.

        Associative Property of Addition: (A + B) + C = A + (B + C)

        Args:
            cast (dict): the game actors {key: tag, value: list}.
        """

        if (choice_list[1] != choice_list[0] and
            choice_list[2] != choice_list[1] and
            choice_list[2] != choice_list[0] and
            choice_list[3] == choice_list[0] and
            choice_list[4] == choice_list[1] and
            choice_list[5] == choice_list[2]
            ):
            return True
        return False

    def mult_id(self, choice_list):
        """
        Method for Multiplication Identity Property: if correct, return True.

        Identity Property of Multiplication: 1 x A = A

        Args:
            cast (dict): the game actors {key: tag, value: list}.
        """

        if (choice_list[0] == 1 and
            choice_list[1] == choice_list[0] and
            choice_list[2] == choice_list[1]
            ):
            return True
        return False

    def mult_commut(self, choice_list):
        """
        Method for Multiplication Commutative Property: if correct, return True.

        Commutative Property of Multiplication: A x B = B x A

        Args:
            cast (dict): the game actors {key: tag, value: list}.
        """

        if (choice_list[1] != choice_list[0] and
            choice_list[2] == choice_list[1] and
            choice_list[3] == choice_list[0]
            ):
            return True
        return False

    def mult_assoc(self, choice_list):
        """
        Method for Multiplication Associative Property: if correct, return True.

        Associative Property of Multiplication: (A x B) x C = A x (B x C)


        Args:
            cast (dict): the game actors {key: tag, value: list}.
        """

        if (choice_list[1] != choice_list[0] and
            choice_list[2] != choice_list[1] and
            choice_list[2] != choice_list[0] and
            choice_list[3] == choice_list[0] and
            choice_list[4] == choice_list[1] and
            choice_list[5] == choice_list[2]
            ):
            return True
        return False

    def mult_add_dist(self, choice_list):
        """
        Method for Distributive Property of Multiplication and Addition:
            if correct, return True.

        Distributive property of multiplication and division:
            N x (A + B) = (N x A) + (N x B)
            where N is a number.
            example:  2 x (A + B) = (2 x A) + (2 x B)

        Args:
            cast (dict): the game actors {key: tag, value: list}.
        """

        # (AH) doesn't matter if chose number/letter or fruit.
        # if (isinstance(choice_list[0], int) and
        #     not isinstance(choice_list[1], int) and
        # if choice_list[1] != choice_list[0] and
        #     choice_list[2] != choice_list[1] and
        if (choice_list[3] == choice_list[0] and
            choice_list[4] == choice_list[1] and
            choice_list[5] == choice_list[0] and
            choice_list[6] == choice_list[2]
            ):
            return True
        return False
