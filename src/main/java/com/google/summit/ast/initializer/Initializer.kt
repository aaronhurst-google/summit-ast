/*
 * Copyright 2022 Google LLC
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.summit.ast.initializer

import com.google.summit.ast.NodeWithSourceLocation
import com.google.summit.ast.SourceLocation
import com.google.summit.ast.TypeRef

/**
 * Abstract base class for initializers.
 *
 * An initializer is an action that occurs after object allocation to setup its initial state. A
 * constructor is a general initializer for classes, but there is also specific initializer syntax
 * to succinctly populate collection types like arrays, sets, lists, and maps.
 *
 * @property type of the initialized object
 * @param loc the location in the source file
 */
sealed class Initializer(val type: TypeRef, loc: SourceLocation) : NodeWithSourceLocation(loc)
