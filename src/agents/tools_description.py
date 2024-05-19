class ToolDescriptions:
    QUERIES = """
        Use this tool to answer general queries of the user, or if the user is asking anything related to his fitness.
        If you are not aware of the exact answer try to answer the question based on context promoting cult without moving on to other tools, only if the context allows.

        Guidelines:

        Address user inquries and inputs as it is, without modifying it on your own. Pass the whole query as it is, without modifying it.
        Respond whatever response you get, without looking for additional information.

        Execution:
        Change the user's input only when you cant find any information from the context as it is.
        Example:

        User Input: "What modes of payment are accepted?"
        Pass it to the function as it is: "What modes of payment are accepted?"

    """

    PRICE = """
        Purpose: Utilize this function to answer specific queries related to pricing information for Cult memberships or services. This function provides redirect links to the website of the gym or Cultpass for detailed pricing information.

        Guidelines:

        Address user inquiries specifically seeking pricing details, including:
        Costs of different Cultpass tiers (Pro, Elite, etc.)
        Pricing details for specific services or classes
        Price comparisons between different membership options
        Execution:

        Pass the user's query to the input exactly as provided without modification.
        Output the response exactly as returned by the function, even if it is just a redirect link to the website.
        Example:

        User Query: "How much does a Cultpass Pro membership cost?"
        Function Response: Provides a redirect link to the pricing page for Cultpass Pro.
    """

    GYM = """
        Purpose:
        Utilize this function to answer specific queries related to gym locations associated with any membership program or specific workout options available. This function provides redirect links to the website of the gym or Cultpass for detailed information.

        Guidelines:

        Address user inquiries specifically seeking details about:
        Gym locations accessible with Cultpass Pro or Elite
        Details about specific gyms (facilities, classes available)
        Different workouts available at specific gyms
        Accessibility of gyms through different Cultpass tiers
        Execution:

        Pass the user's query to the input exactly as provided without modification.
        Output the response exactly as returned by the function, even if it is just a redirect link to the website.
        Example:

        User Query: "Which gyms can I access through Cultpass Pro?"
        Function Response: Provides a redirect link to the relevant page listing gyms accessible with Cultpass Pro.
    """
